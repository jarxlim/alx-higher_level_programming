#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: the head of the linked list
 * @number: data in the new node
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *first;

	first = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || first->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (first->next != NULL)
	{
		if ((first->next->n > new->n && first->n < newnode->n)
			|| new->n == first->n)
		{
			new->next = first->next;
			first->next = new;
			return (new);
		}
		first = first->next;
	}
	new->next = first->next;
	first->next = new;
	return (new);
}
