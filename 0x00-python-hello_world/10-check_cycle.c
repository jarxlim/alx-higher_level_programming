#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - function that checks if a singly linked list has a cycle insied
 * @list: singly linked list
 * Return: 0 if no cycle, 1 if cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *end;

	if (list == NULL)
	{
		return (0);
	}
	head = list;
	end = list;

	while (end != NULL && end->next != NULL)
	{
		head = head->next;
		end = end->next->next;

		if (head == end)
		{
			return (1);
		}
	}
	return (0);
}
