		global _start

		section .text

open_input:	mov	rax, 2
		mov	rsi, inputmode
		syscall
		ret

close_input:	mov	rax, 3
		syscall
		ret

read_file:	mov	rdi, inputfn
		call	open_input
		mov	r12, rax			; save input file handle
		mov	rax, 0				; syscall 0 - sys_read
		mov	rdi, r12			; set file handle
		mov	rsi, inputfile			; read input file into bss section
		mov	rdx, bufsize			; ask to read bufsize bytes
		syscall					; call sys_read
		mov	[filesize], ax			; save number of bytes actually read
		mov	rdi, inputfile
		add	rdi, rax
		mov	rdi, r12			; input filehandle is still in r12, prepare to close
		call	close_input
		ret

;; Get priority of the character in al, return in al
;; ON ENTRY:	al contains the character form of the item
;; ON EXIT:	al has been converted to a priority
get_priority:
		cmp	al, 90				; not great, but bifurcate -- above 90 is a lowercase letter
		jg	.lowercase			; if not, assume uppercase
		sub	al, 38				; difference between A and 27
		ret
.lowercase:	sub	al, 96				; difference between a and 1
		ret

;; Find the (first, only) common element in both compartments of a backpack (a single line in our input)
;; ON ENTRY:	rsi points to the beginning of the input line to check
;; ON EXIT:     rsi points to the beginning of the next input line
;;		rax contains the priority of the duplicated item
find_duplicate_item:
		push	rdi				; we need to preserve rdi
		mov	rdi, rsi			; get rdi to the beginning of the line
		xor	eax, eax			; don't want trash in high bytes of rax
		mov	al, 0x0a			; get ready to scan for \n
		push	rcx				; may as well preserve rcx for the sake of politeness
.find_end:	scasb
		jnz	.find_end
		push	rdi				; save pointer to next line on the stack, we'll restore it on exit
		dec	rdi				; back out \n char
		sub	rdi, rsi			; subtract source from end to get length
		shr	rdi, 1				; divide by 2 for length of each compartment
		mov	rcx, rdi			; store length in rcx
		add	rdi, rsi			; position rdi at start of second half
.outer_loop:	lodsb					; get character from first string to scan for
		push	rdi				; save pointer to beginning of second string
		push	rcx				; preserve string length
		repnz	scasb				; scan rcx bytes of second string to check for duplicate
		jz	.found				; exit if we found a duplicate item
		pop	rcx				; reload string length
		pop	rdi				; reposition rdi to start of second string
		jmp	.outer_loop			; repeat until found
.found:		pop	rcx				; not that it matters, but, yes
		pop	rdi				; don't care really but get rdi back too
		call	get_priority			; al has the duplicate item but we need to convert to priority	
		pop	rsi				; get start of next line into rsi for return
		pop	rcx				; be polite
		pop	rdi				; be polite - rdi needs to point to the end of the file still
		ret

;; Loop through each line of input, summing priorities
;; ON ENTRY:	file is read into buffer, filesize represents the size of the file read
;; ON EXIT:	rbx contains the total score.  rax, rsi, and rdi aren't preserved.
loop_until_end:	mov	rsi, inputfile			; position rsi to the start of input
		mov	rdi, rsi
		xor	eax, eax			; clear high bytes of rax
		mov	ax, WORD [filesize]		; get input file size
		add	rdi, rax			; store the end position in rdi
		xor	rbx, rbx			; keep the running total in rbx
.loop:		call	find_duplicate_item
		xor	ah, ah				; clear high byte of ax (opponent's hand, no need to preserve)
		add	bx, ax				; round returns score in al, add to running total
		cmp	rsi, rdi			; check if we're done
		jl	.loop				; otherwise, play next round
		ret					; if we're done, return leaving the total score in rbx

;; Format and display result
;; ON ENTRY:	rbx contains the total score
;; ON EXIT:	most registers are trashed, sorry.  the result has been printed to STDOUT
display_result:	mov	rax, 1
		mov	rdi, 1
		mov	rsi, msg1
		mov	rdx, msg1len
		syscall
		std
		mov	cx, 1
		mov	rax, rbx
		mov	rdi, numstringend
		mov	ebx, 10
.loop:		xor	edx, edx	
		div	ebx
		push	rax
		mov	al, dl
		add	al, '0'
		stosb
		inc	cx
		pop	rax
		test	eax, eax
		jnz	.loop
		cld
		mov	rax, 1	
		mov	rsi, 1
		xchg	rsi, rdi
		xor	edx, edx
		mov	dx, cx
		syscall
		mov	rax, 1
		mov	rdi, 1
		mov	rsi, msg2
		mov	rdx, msg2len
		syscall
		ret

error_exit:	mov	edi, 1
		jmp	exit
success_exit:	xor	edi, edi
exit:		mov	rax, 60				; set up for exit syscall
		syscall

_start:		call	read_file			; read in the input file
		call	loop_until_end			; play all rounds, get total score into rbx
		call	display_result			; display a message containing the score to STDOUT
		jmp 	success_exit

		section .data
inputfn:	db	"day03.txt", 0
inputmode:	equ	0
msg1:		db	"Sum of the priorities is: "
msg1len:	equ	$ - msg1
msg2:		db	0x0a
msg2len:	equ	$ - msg2

		section .bss
inputfile:	resb	65535
bufsize:	equ	$ - inputfile
filesize:	resw	1
numstring:	resb	16
numstringend:	equ	$ - 1
