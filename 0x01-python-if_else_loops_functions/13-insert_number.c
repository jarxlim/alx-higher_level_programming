#include "lists.h"

/**
 * insert_node - function that adds a number into a singly-linked list.
 * @head: the head of the linked list.
 * @number: number to insert.
 * Return: 0 function fails or pointer to the newnode node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;

	if (node == NULL || node->n >= number)
	{
		newnode->next = node;
		*head = newnode;
		return (newnode);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	newnode->next = node->next;
	node->next = newnode;

	return (newnode);
}
