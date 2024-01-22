#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head;
    listint_t *slow = *head;
    listint_t *prev_slow = NULL;
    listint_t *second_half = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list
        listint_t *temp = slow;
        slow = slow->next;
        temp->next = prev_slow;
        prev_slow = temp;
    }

    // If the number of elements is odd, move slow to the next element
    if (fast != NULL)
        slow = slow->next;

    second_half = slow;

    // Compare the reversed first half with the second half
    while (prev_slow != NULL && second_half != NULL)
    {
        if (prev_slow->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }

        prev_slow = prev_slow->next;
        second_half = second_half->next;
    }

    // Restore the original list
    while (prev_slow != NULL)
    {
        listint_t *temp = prev_slow->next;
        prev_slow->next = slow;
        slow = prev_slow;
        prev_slow = temp;
    }

    *head = slow; // Update the head of the list

    return is_palindrome;
}

