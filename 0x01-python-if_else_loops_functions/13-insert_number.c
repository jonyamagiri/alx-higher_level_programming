#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: list head
* @number: number to store in the new node
* Return: NULL (if it failed), the address of the new node (otherwise)
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new_node;

	temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	for (; temp->next != NULL; temp = temp->next)
	{
		if ((temp->next)->n >= number)
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
	}

	new_node->next = NULL;
	temp->next = new_node;
	return (new_node);
}
