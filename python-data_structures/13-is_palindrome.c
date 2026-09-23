#include "lists.h"

/**
 * is_palindrome - checks whether a singly linked list is a palindrome
 * @head: pointer to the list head
 *
 * Return: 1 if the list is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *previous;
	listint_t *second, *middle, *reversed;
	listint_t *left, *right;
	int palindrome = 1;

	if (head == NULL || *head == NULL)
		return (1);

	slow = *head;
	fast = *head;
	previous = NULL;

	/* Find the beginning of the second half of the list. */
	while (fast != NULL && fast->next != NULL)
	{
		previous = slow;
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Skip the middle node when the list has an odd length. */
	middle = NULL;
	if (fast != NULL)
	{
		middle = slow;
		second = slow->next;
	}
	else
		second = slow;

	/* Reverse the second half so it can be compared with the first half. */
	reversed = NULL;
	while (second != NULL)
	{
		listint_t *next = second->next;

		second->next = reversed;
		reversed = second;
		second = next;
	}

	left = *head;
	right = reversed;
	while (right != NULL)
	{
		if (left->n != right->n)
		{
			palindrome = 0;
			break;
		}
		left = left->next;
		right = right->next;
	}

	/* Restore the list before returning. */
	second = NULL;
	while (reversed != NULL)
	{
		listint_t *next = reversed->next;

		reversed->next = second;
		second = reversed;
		reversed = next;
	}

	if (middle != NULL)
		middle->next = second;
	else if (previous != NULL)
		previous->next = second;

	return (palindrome);
}
