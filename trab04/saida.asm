.text
	li $t0,0
	move $s1,$t0
	li $v0, 5
	syscall
	move $s2,$v0
L1:
	li $t1,1
	blt $s1,$s2,L0
	li $t1,0
L0:	beq $t1,0,L2
	li $v0, 1
	move $a0,$s1
	syscall
	li $v0,11
	li $a0,'\n'
	syscall
	li $t2,1
	add $t3,$s1,$t2
	move $s1,$t3
	j L1
L2:
