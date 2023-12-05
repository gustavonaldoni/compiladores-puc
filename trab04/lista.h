char instrucao[30];

void createCode(char **codigo) {
  	*codigo = (char *) malloc(1);
  	strcpy(*codigo,"");
}

void insertCode(char **codigo, char *instrucao) {
	char *aux;
  	aux = *codigo;
  	*codigo = (char *) malloc(strlen(*codigo)+strlen(instrucao)+2);
  	strcpy(*codigo,aux);
  	strcat(*codigo,instrucao);
  	free(aux);
}

void printCode(char *codigo) {
  	printf("%s",codigo);
}

