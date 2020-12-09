#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - frees a listint_t list
 * @head: pointer to list to be freed
 * @number: argument
 * Return: node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux = NULL;
	listint_t *node = NULL;

	if (*head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	node->next = NULL;
	node->n = number;
	aux = *head;

	while (aux)
	{
		if (aux->n >= number)
		{
			node->next = aux;
			*head = node;
			return (node);
		}
		if (aux->next->n >= number)
		{
			if (aux->next)
			{
				node->next = aux->next;
				aux->next = node;
				return (node);
			}
		}
		aux = aux->next;
	}
	free(node);
	return (NULL);


}
