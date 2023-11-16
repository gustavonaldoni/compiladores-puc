#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 20

struct no
{
    char dado[MAX];
    struct no *prox;
};

typedef struct
{
    struct no *primeiro;
    struct no *ultimo;
} lista;

void l_criar(lista *);
int l_destruir(lista *);

int l_estaVazia(lista);
void l_mostrar(lista);

char *l_primeiro(lista);
char *l_ultimo(lista);

int l_tamanho(lista);
int l_tamanhoBytes(lista);

int l_inserir(lista *, char *);
void l_remover(lista *, char *);
void l_removerTodos(lista *, char *);

int l_contar(lista, char *);
int l_substituir(lista *, char *, char *);

void l_concatenarListas(lista *, lista *);

void l_criar(lista *l)
{
    l->primeiro = NULL;
    l->ultimo = NULL;
}

int l_destruir(lista *l)
{
    struct no *aux;

    if (l_estaVazia(*l))
        return 0;

    aux = l->primeiro;

    while (aux != NULL)
    {
        l_remover(l, aux->dado);
        aux = l->primeiro;
    }

    return 1;
}

int l_estaVazia(lista l)
{
    return l.primeiro == NULL &&
           l.ultimo == NULL;
}

void l_mostrar(lista l)
{
    struct no *aux;

    if (l_estaVazia(l))
    {
        printf("lista vazia ...\n");
        return;
    }

    aux = l.primeiro;

    while (aux != NULL)
    {
        printf("%s ", aux->dado);
        aux = aux->prox;
    }
}

char *l_primeiro(lista l)
{
    if (l_estaVazia(l))
        return NULL;

    return l.primeiro->dado;
}

char *l_ultimo(lista l)
{
    if (l_estaVazia(l))
        return NULL;

    return l.ultimo->dado;
}

int l_tamanho(lista l)
{
    int contador = 0;
    struct no *aux;

    if (l_estaVazia(l))
        return 0;

    aux = l.primeiro;

    while (aux != NULL)
    {
        contador += 1;
        aux = aux->prox;
    }

    return contador;
}

int l_tamanhoBytes(lista l)
{
    int numeroElementos = l_tamanho(l);

    return (size_t)(sizeof(l) + numeroElementos * sizeof(struct no));
}

int l_inserir(lista *l, char *dado)
{
    struct no *aux;

    aux = (struct no *)malloc(sizeof(struct no));

    if (aux == NULL)
        return 0;

    strcpy(aux->dado, dado);

    if (l_estaVazia(*l))
    {
        l->primeiro = aux;
        l->ultimo = aux;

        aux->prox = NULL;

        return 1;
    }

    l->ultimo->prox = aux;
    aux->prox = NULL;
    l->ultimo = aux;

    return 1;
}

void l_remover(lista *l, char *dado)
{
    struct no *aux, *anterior, *atual;

    if (l_estaVazia(*l))
        return;

    // Remover único elemento de lista unitária
    if (l->primeiro == l->ultimo && l->primeiro != NULL && strcmp(l->primeiro->dado, dado) == 0)
    {
        aux = l->primeiro;

        l->primeiro = NULL;
        l->ultimo = NULL;

        free(aux);
    }

    // Remover primeiro elemento de lista não unitária
    if (l->primeiro != l->ultimo && strcmp(l->primeiro->dado, dado) == 0)
    {
        aux = l->primeiro;

        l->primeiro = l->primeiro->prox;

        free(aux);
    }

    // Remover elemento de qualquer outra posição da lista
    anterior = l->primeiro;
    atual = anterior->prox;

    while (strcmp(atual->dado, dado) != 0 && atual->prox != NULL)
    {
        anterior = atual;
        atual = atual->prox;
    }

    if (atual == NULL)
        return;

    // Chegou no último elemento da lista
    else if (atual->prox == NULL)
    {
        aux = atual;

        anterior->prox = NULL;
        l->ultimo = anterior;

        free(aux);
    }

    else
    {
        aux = atual;

        anterior->prox = atual->prox;

        free(aux);
    }
}

void l_removerTodos(lista *l, char *dado)
{
    int i;
    int repeticoes = l_contar(*l, dado);

    if (repeticoes == 0)
        return;

    for (i = 0; i < repeticoes; i++)
        l_remover(l, dado);
}

int l_contar(lista l, char *dado)
{
    int contador = 0;
    struct no *aux;

    if (l_estaVazia(l))
        return 0;

    aux = l.primeiro;

    while (aux != NULL)
    {
        if (strcmp(aux->dado, dado) == 0)
            contador += 1;

        aux = aux->prox;
    }

    return contador;
}

int l_substituir(lista *l, char *dadoOrigem, char *dadoDestino)
{
    struct no *aux;

    if (l_estaVazia(*l))
        return 0;

    aux = l->primeiro;

    while (aux != NULL)
    {
        if (strcmp(aux->dado, dadoOrigem) == 0)
        {
            strcpy(aux->dado, dadoDestino);
            return 1;
        }

        aux = aux->prox;
    }

    return 0;
}

void l_concatenarListas(lista *lista1, lista *lista2)
{
    if (l_estaVazia(*lista1) || l_estaVazia(*lista2))
        return;

    lista1->ultimo = lista2->primeiro;
}