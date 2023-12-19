#   Advent of Code 2023
#      GiantWaffle
#   Challenge 19 of 25
#      Part 2 of 2
# -----------------------

use_real_data = False
data = []

with open('Day19\data_day19.txt') as f:
   lines = f.readlines()
   for line in lines:
      data.append(line.strip())

example = [
    'px{a<2006:qkq,m>2090:A,rfg}', #[px, [a, <, 2006, qkq],[m, >, 2090, A], rfg]
    'pv{a>1716:R,A}',
    'lnx{m>1548:A,A}',
    'rfg{s<537:gd,x>2440:R,A}',
    'qs{s>3448:A,lnx}',
    'qkq{x<1416:A,crn}',
    'crn{x>2662:A,R}',
    'in{s<1351:px,qqz}',
    'qqz{s>2770:qs,m<1801:hdj,R}',
    'gd{a>3333:R,R}',
    'hdj{m>838:A,pv}',
    '',
    '{x=787,m=2655,a=1222,s=2876}', #[787, 2655, 1222, 2876]
    '{x=1679,m=44,a=2067,s=496}',
    '{x=2036,m=264,a=79,s=2244}',
    '{x=2461,m=1339,a=466,s=291}',
    '{x=2127,m=1623,a=2188,s=1013}'
]

if use_real_data:
    test_input = data
else:
    test_input = example


# ! [px, [a, <, 2006, qkq],[m, >, 2090, A], rfg]
    
ins_count = 11 #11 for test -  509 for real
instructions = []

for i in range(ins_count):
    full_instruction = []
    line = test_input[i]
    name = line.split('{')[0]
    ins = line.split('{')[1][:-1]
    ins = ins.split(',')
    dest = ins[-1]
    ins = ins[:-1]

    full_instruction.append(name)

    for part in ins:
        iden = part[:1]
        op = part[1:2]
        num = int(part.split(':')[0][2:])
        des = part.split(':')[1]
        part_list = [iden, op, num, des]
        full_instruction.append(part_list)

    full_instruction.append(dest)
    instructions.append(full_instruction)

ins_dict = {}

for ins in instructions:
    ins_dict[ins[0]] = ins[1:]


# ! List = [X, M, A, S]

objects = []

for k in range(ins_count+1, len(test_input)):
    fin = []
    line_num = k
    fin = test_input[line_num][1:-1].split(',')
    fin = [int(item[2:]) for item in fin]
    objects.append(fin)

# for obj in objects:
#     print(obj)
    
def proc_ins(ins, com):
    ins_input = ins[0]
    op = ins[1]
    num = ins[2]
    dest = ins[3]

    if op == '<': #less
        match ins_input:
            case 'x':
                if com[0] < num:
                    return dest
            case 'm':
                if com[1] < num:
                    return dest
            case 'a':
                if com[2] < num:
                    return dest
            case 's':
                if com[3] < num:
                    return dest
        return None
    else: #gt
        match ins_input:
            case 'x':
                if com[0] > num:
                    return dest
            case 'm':
                if com[1] > num:
                    return dest
            case 'a':
                if com[2] > num:
                    return dest
            case 's':
                if com[3] > num:
                    return dest
        return None


accepted = []
rejected = []

current_ins = 'in'

q = []

for obj in objects: #add all objects to queue
    q.append(obj)

while(len(q) > 0):
    if current_ins == 'A':
        accepted.append(q[0])
        print(f'Adding {q[0]} to Accepted')
        q.pop(0)
        current_ins = 'in'
        continue

    if current_ins == 'R':
        rejected.append(q[0])
        print(f'Adding {q[0]} to Rejected')
        q.pop(0)
        current_ins = 'in'
        continue

    last = ins_dict[current_ins][-1]
    steps = ins_dict[current_ins][:-1]

    #print(f'OBJ: {q[0]}')
    for step in steps:
        #print(step)
        result = proc_ins(step, q[0])
        #print(result)
        if result != None:
            current_ins = result
            #print(f'Changing ins to: {current_ins}')
            break
    else:
        current_ins = last
        
total = 0

for accept in accepted:
    total += sum(accept)

print(f'Part 1 Answer: {total}')