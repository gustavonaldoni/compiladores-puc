	li $t0, 10
	move $s1, $t0
	li $t1, 20
	move $s2, $t1
	li $t2, 30
	add $t3, $t2, $s1
	add $t4, $t3, $s2
	move $s3, $t4
	li $v0, 1
	move $a0, $s3
	syscall
