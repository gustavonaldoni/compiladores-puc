	li $t0, 10
	move $s1, $t0
	li $t1, 20
	move $s2, $t1
	li $t2, 1
	bgt $s1, $s2, L1
	li $t2, 0
L1:	move $s3, $t2
	li $t3, 1000
	li $t4, 1
	bge $s1, $t3, L2
	li $t4, 0
L2:	move $s3, $t4
	li v0, 1
	move $a0, $s3
	syscall
