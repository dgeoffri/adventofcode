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

;; Read a line from the input and return as an integer in rax
;; ON ENTRY:    rsi points to current position in input
;; ON EXIT:     rsi points to beginning of next line to consume
;;		al contains the points earned this round
play_round:	xor	eax, eax			; clear the high bytes of rax
		lodsb					; get the other player's hand
							; TODO: validate this input and error out if out if invalid
		sub	al, '@'				; A=1, etc.
		mov	ah, al				; move off to the side
		lodsb					; get the "space" between the characters
		cmp	al, ' '				; make sure it's a space (primitive sanity check)
		jne	error_exit			; exit with error code set if not
		lodsb					; get hand to play
							; TODO: validate this input and error out if out if invalid
		sub	al, 'W'				; X=1, etc.
		call	score_round			; I don't know about you, but part of me is just happy how much
							; of this part would work fine on an old 8088
		cmp	BYTE [rsi], 0x0a			; make sure the next char is newline, sanity check
		jne	error_exit			; exit angrily if not
		inc	rsi				; move pointer to beginning of next line
		ret					; return

;; Score the current match and return the score
;; ON ENTRY:	ax contains both hands, with the other player's hand in ah and the hand to be played in al
;; ON EXIT:	al contains the number of points to score.  ah is not preserved
score_round:	cmp	ah, al				; if both hands are equal, it's a tie
		je	.tie
		inc	ah
		cmp	ah, al				; if opponent's hand is one lower, we win
		je	.win
		cmp	al, 1				; if our hand is rock
		jne	.lose
		cmp	ah, 4				; and opponent had scissors (prior to being incremented)
		jne	.lose				; we also win
.win:		add	al, 3				; winning hand gets +6 but we're going to fall through so 3 now 3 later
.tie:		add	al, 3				; draw adds 3 points to our score
.lose:		ret					; losing round just gets the value of the hand

;; Play all rounds and keep score
;; ON ENTRY:	file is read into buffer, filesize represents the size of the file read
;; ON EXIT:	rbx contains the total score.  rax, rsi, and rdi aren't preserved.
play_to_end:	mov	rsi, inputfile			; position rsi to the start of input
		mov	rdi, rsi
		xor	eax, eax			; clear high bytes of rax
		mov	ax, WORD [filesize]		; get input file size
		add	rdi, rax			; store the end position in rdi
		xor	rbx, rbx			; keep the running total in rbx
.loop:		call	play_round
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
		call	play_to_end			; play all rounds, get total score into rbx
		call	display_result			; display a message containing the score to STDOUT
		jmp 	success_exit

		section .data
inputfn:	db	"day02.txt", 0
inputmode:	equ	0
msg1:		db	"You've ended up with "
msg1len:	equ	$ - msg1
msg2:		db	" points", 0x0a
msg2len:	equ	$ - msg2

		section .bss
inputfile:	resb	65535
bufsize:	equ	$ - inputfile
filesize:	resw	1
numstring:	resb	16
numstringend:	equ	$ - 1
