# people = [{
#         'name':'Miguel',
#         'spent' : 30,
#         'has_to_recieve':0,
#         'split': []
# },
# {
#         'name':'Omar',
#         'spent' : 20,
#         'has_to_recieve':0,
#         'split': []
# },
# {
#         'name':'Stefi',
#         'spent' : 12,
#         'has_to_recieve':0,
#         'split': []
# },
# {
#         'name':'Alessandra',
#         'spent' : 10,
#         'has_to_recieve':0,
#         'split': []
# },
# {
#         'name':'gabriel',
#         'spent' : 0,
#         'has_to_recieve':0,
#         'split': []
# }]

# # person = {

# #         'name':'Name',
# #         'spent' : 200,
# #         'has_to_recieve':0,
# #         'split': []

# #     }



# total = 0

# for person in people:
#     total = total + person["spent"]


# individual_payment = total/len(people)


# have_to_pay = []
# have_to_recieve = []


# for person in people:
#     person['has_to_recieve'] = person["spent"] - individual_payment

#     if(person['has_to_recieve']>=0):
#         have_to_recieve.append(person)
#     else:
#         have_to_pay.append(person)


# have_to_pay.sort(key=lambda person: person['has_to_recieve'], reverse=True)

# have_to_recieve.sort(key=lambda person: person['has_to_recieve'])


# for person in have_to_pay:
#     while abs(person['has_to_recieve'])>0 and len(have_to_recieve)>0:

#         if(abs(person['has_to_recieve'])<=have_to_recieve[0]['has_to_recieve']):

#             person['split'].append({
#                 'name': have_to_recieve[0]['name'],
#                 'amount': abs(person['has_to_recieve'])

#             })

#             have_to_recieve[0]['has_to_recieve'] = have_to_recieve[0]['has_to_recieve'] + person['has_to_recieve']

#             person['has_to_recieve'] = 0

#         else: 
#             person['split'].append({
#                 'name': have_to_recieve[0]['name'],
#                 'amount': have_to_recieve[0]['has_to_recieve'], 



#             })

#             person['has_to_recieve'] = person['has_to_recieve'] + have_to_recieve[0]['has_to_recieve']
#             have_to_recieve[0]['has_to_recieve']= 0
#             have_to_recieve.remove(have_to_recieve[0])
#             print("remove")

# for x in have_to_pay:
#     print(x)