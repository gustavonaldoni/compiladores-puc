char instrucao[30];

void create_cod(char **codigo) {
  *codigo = (char *) malloc(1);
  strcpy(*codigo,"");
}

void insert_cod(char **codigo, char *instrucao) {
  char *aux;
  aux = *codigo;
  *codigo = (char *) malloc(strlen(*codigo)+strlen(instrucao)+2);
  strcpy(*codigo,aux);
  strcat(*codigo,instrucao);
  free(aux);
}

void print_cod(char *codigo) {
  printf("%s",codigo);
}


