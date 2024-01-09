#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow, *mid, *second_half;
    int palindrome = 1;

    slow = *head;
    fast = *head;

    if (*head != NULL && (*head)->next != NULL)
    {
        /* Find the middle of the list using slow and fast pointers */
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        /* If the number of elements is odd, skip the middle element */
        if (fast != NULL)
        {
            mid = slow;
            slow = slow->next;
        }

        /* Reverse the second half of the list */
        second_half = slow;
        prev_slow->next = NULL; /* Disconnect the first half from the second half */
        reverse_list(&second_half);

        /* Compare the reversed second half with the first half */
        palindrome = compare_lists(*head, second_half);

        /* Restore the original list by reversing the second half again */
        reverse_list(&second_half);

        /* If the number of elements was odd, reconnect the middle element */
        if (mid != NULL)
        {
            prev_slow->next = mid;
            mid->next = second_half;
        }
        else
        {
            prev_slow->next = second_half;
        }
    }

    return palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev, *current, *next;

    prev = NULL;
    current = *head;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return 0;
        list1 = list1->next;
        list2 = list2->next;
    }

    return 1;
}
