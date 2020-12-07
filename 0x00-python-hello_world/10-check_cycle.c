#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
	listint_t *initpointer;
	listint_t *detect_pointer;

	if (list == NULL)
		return (0);
	initpointer = list;
	detect_pointer = list;
	while (list)
	{
		detect_pointer = detect_pointer->next->next;
		initpointer = initpointer->next;
		if (!detect_pointer || !initpointer)
			return (0);
		if (detect_pointer == initpointer)
			return (1);
	}
	return (0);
}
