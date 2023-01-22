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
		mov	al, 10
		stosb					; hack, need one more newline
		mov	rdi, r12			; input filehandle is still in r12, prepare to close
		call	close_input
		ret

;; Read a line from the input and return as an integer in rax
;; ON ENTRY:    rsi points to current position in input
;; ON EXIT:     rsi points to beginning of next line to consume
;;		rax contains numerical value read, or 0 if empty line.  caller determines
;;		    empty line case by determining that rsi has only advanced one byte
read_number:	push	rdx
		push	rbx
		xor	edx, edx			; zero out running total of digits
		xor	eax, eax			; clear the high bytes of rax
.loop:		lodsb
		cmp	al, 0x0a			; check for newline
		jz	.done				; return if end of line reached
		
		imul    edx, 10				; otherwise it's a digit, multiply existing total by 10 and add
		sub	al, '0'				; convert ascii to integer
		add	edx, eax			; add to running total
		jmp	.loop				; continue to read digits
.done:		mov	rax, rdx			; return total in rax
		pop	rbx				; restore rbx
		pop	rdx				; restore rdx
		ret					; return

findmax:	cld
		mov	rsi, inputfile
		push	rbx
.outerloop:	mov	rdi, inputfile
		add	di, [filesize]
		cmp	rsi, rdi
		jae	.done				; make sure we haven't advanced beyond EOF
		xor	edx, edx			; zero out running total
.innerloop:	mov	rdi, rsi
		call	read_number
		inc	rdi
		cmp	rdi, rsi
		je	.groupdone			; if rsi is only one byte further than before, end of group
		add	rdx, rax			; add line to running total
		jmp	.innerloop			; get next line
.groupdone:	cmp	rdx, [largest3]			; less than the third-best?
		jle 	.outerloop			; then continue
		mov	[largest3], rdx			; else replace third spot
		cmp	rdx, [largest2]			; less than second-best?
		jle 	.outerloop			; then continue
		mov	rbx, [largest2]			; else shuffle middle position down
		mov	[largest3], rbx
		mov	[largest2], rdx			; and replace
		cmp	rdx, [largest1]			; less than all-time best?
		jle 	.outerloop			; then continue
		mov	rbx, [largest1]			; else shuffle top position down
		mov	[largest2], rbx
		mov	[largest1], rdx			; and replace
		jmp	.outerloop			; and continue
.done:		pop	rbx
		ret

display_result:	mov	rax, 1
		mov	rdi, 1
		mov	rsi, msg1
		mov	rdx, msg1len
		syscall
		std
		mov	cx, 1
		mov	rax, [largest1]
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

disp_result2:	mov	rax, 1
		mov	rdi, 1
		mov	rsi, msg3
		mov	rdx, msg3len
		syscall
		std
		mov	cx, 1
		mov	rax, [largest1]
		add	rax, [largest2]
		add	rax, [largest3]
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

success_exit:	xor	edi, edi			; only successful exits implemented
exit:		mov	rax, 60				; set up for exit syscall
		syscall

_start:		call	read_file
		call	findmax
		call	display_result
		call	disp_result2
		jmp 	success_exit

		section .data
inputfn:	db	"day01.txt", 0
inputmode:	equ	0
largest1:	dq	0
largest2:	dq	0
largest3:	dq	0
msg1:		db	"The elf with the most calories has "
msg1len:	equ	$ - msg1
msg2:		db	" calories.", 0x0a
msg2len:	equ	$ - msg2
msg3:		db	"The sum of the calories carried by the top 3 elves is "
msg3len:	equ	$ - msg3

		section .bss
inputfile:	resb	65535
bufsize:	equ	$ - inputfile
filesize:	resw	1
numstring:	resb	16
numstringend:	equ	$ - 1
