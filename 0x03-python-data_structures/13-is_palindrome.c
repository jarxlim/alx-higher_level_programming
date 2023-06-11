#include "lists.h"

/**
 * is_palindrome - function to check if a linked list is a palindrome
 * @head: head of the list
 * Return: 1 if its palindrome, 0 if its not
 */

int is_palindrome(listint_t **head)
{
	listint_t *present_node;
	char buff[10000];
	int i, len = 0;

	if (!*head || !head)
	{
		return (1);
	}
	present_node = *head;
	if (!present_node->next)
	{
		return (1);
	}
	while (present_node)
	{
		buff[len] = present_node->n;
		present_node = present_node->next;
		len++;
	}
	len = len - 1;
	for (; len >= 0 && i <= len; len--, i++)
	{
		if (buff[len] != buff[i])
			return (0);
	}
	return (1);
}
