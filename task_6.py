types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_double(tickets):
    unique = []
    result = {}
    for i, ticket_list in tickets.items(): 
        fresh_tickets = [] 
        for ticket in ticket_list:
            if ticket not in unique:
                unique.append(ticket)
                fresh_tickets.append(ticket)
        result[i] = fresh_tickets
    return result

processed_tickets = delete_double(tickets)

def conect_types_unic_tickets(types, tickets): 
    result = {}
    for k,v in types.items():
        result[v] = tickets[k]
    return result

tickets_by_type = conect_types_unic_tickets(types, processed_tickets)

print(tickets_by_type)