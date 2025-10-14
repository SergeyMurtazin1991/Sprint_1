tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

def delete_duplicate_tickets(tickets):
    existing_tickets = []
    tickets_without_duplicate = {}
    for number, tickets_lst in tickets.items():
        tickets_without_duplicate[number] = []
        for ticket in tickets_lst:
            if ticket not in existing_tickets:
                tickets_without_duplicate[number].append(ticket)
            existing_tickets.append(ticket)
    return tickets_without_duplicate

def connect_tickets_with_severity_types(types, tickets):
    connected_tickets = {}
    for type_number, type in types.items():
        for number, tickets_lst in tickets.items():
            if number == type_number:
                connected_tickets[type] = tickets_lst
                continue
    return connected_tickets

tickets_without_duplicate = delete_duplicate_tickets(tickets)
connected_tickets = connect_tickets_with_severity_types(types, tickets_without_duplicate)
print(tickets_without_duplicate)
print(connected_tickets)#