#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - is palindrome
 * @head: head node
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
        listint_t *current = *head;
        int tmp[100], i = 0, s = 0;

        if (!*head || !head || !current->next)
                return (1);

        while (current)
        {
            tmp[i] = current->n;
            i++;
            current = current->next;
        }
        i--;
        while (s <= i)
        {
            if(tmp[s] != tmp[i])
                return (0);
            s++;
            i--;
        }
        return (1);
}
