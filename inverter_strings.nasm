global _start
section .text

_start:
	mov rsi, [rsp + 16] 
	xor rdx, rdx
	xor rcx, rcx

loop: 
	mov bl, [rsi + rdx]
	inc rdx
	test bl, bl
	jnz loop
	
	lea rdi, [rsi + rdx - 1]
	
	inv_bytes_loop:
	cmp rsi, rdi
	jae inv_bytes_done
	add rcx, 1
	mov bh, [rsi]
	mov ah, [rdi]
	mov [rdi], bh
	mov [rsi], ah
	inc rsi
	dec rdi
	jmp inv_bytes_loop
	
	inv_bytes_done:
	sub rsi, rcx
	mov rax, 1
	mov rdi, 1
	syscall

	mov rax, 1
	mov rsi, line_break
	mov rdi, 1
	syscall

	mov rax, 60
	mov rdi, 0
	syscall

section .data
line_break:
	db 0xa
