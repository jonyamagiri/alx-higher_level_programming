#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: linked list head
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slowptr, *fastptr;

	if (list == NULL || list->next == NULL)
		return (0);

	slowptr = list;
	fastptr = list->next;

	while (slowptr != fastptr)
	{
		if (fastptr == NULL || fastptr->next == NULL)
		{
			return (0);
		}
		slowptr = slowptr->next;
		fastptr = fastptr->next->next;
	}
	return (1);
}
