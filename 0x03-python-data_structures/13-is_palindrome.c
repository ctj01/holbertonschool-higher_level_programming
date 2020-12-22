#include "lists.h"
/**
 * is_palindrome - is palindrome
 * @head: head node
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
        listint_t *aux = *head;
        int data[150], i = 0, d = 0;

        if (!*head || !head || !aux->next)
                return (1);

        while (aux)
        {
            data[i] = aux->n;
            i++;
            aux = aux->next;
        }
        i--;
        while (d <= i)
        {
            if(data[d] != data[i])
                return (0);
            d++;
            i--;
        }
        return (1);
}
