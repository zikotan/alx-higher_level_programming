#include "lists.h"

/**
 * check_cycle - the check_cycle function
 * @list: pointer to the list
 *
 * Return: 1 if there is a cycle,
 * 1 if there isn't.
 */
int check_cycle(listint_t *list)
{
	listint_t *list1;
	listint_t *list2;

	list1 = list;
	list2 = list;
	while (list && list1 && list1->next)
	{
		list = list->next;
		list1 = list1->next->next;

		if (list == list1)
		{
			list = list2;
			list2 =  list1;
			while (1)
			{
				list1 = list2;
				while (list1->next != list && list1->next != list2)
				{
					list1 = list1->next;
				}
				if (list1->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
