#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Function to insert number in a sorted linked list
 * @head: Pointer to pointer to head of listint_t
 * @number: Number to be inserted
 * Return: Pointer to the head
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *prev = *head;
	listint_t *new_node;

	new_node = (listint_t*)malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}

	while (temp->next != NULL)
	{
		if (temp->n > number)
		{
			prev->next = new_node;
			new_node->next = temp;
			return (new_node);
		}
		prev = temp;
		temp = temp->next;
	}
	if (temp->next == NULL)
	{
		temp->next = new_node;
		new_node->next = NULL;
	}
	free(new_node);
	return (NULL);
}
