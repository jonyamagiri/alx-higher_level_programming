#include "lists.h"

/**
* is_palindrome - determines if a singly linked list is a palindrome
* @head: pointer to head of singly linked list
* Return: 1 (if palindrome), 0 (otherwise)
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	unsigned int size = 0, i = 0;
	int data[20480];

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	for (; temp; size++)
	{
		temp = temp->next;
	}
	if (size == 1)
		return (1);

	temp = *head;
	while (temp)
	{
		data[i++] = temp->n;
		temp = temp->next;
	}

	for (i = 0; i <= (size / 2); i++)
	{
		if (data[i] != data[size - i - 1])
		return (0);
	}
	return (1);
}
