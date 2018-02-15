def rumorReport(studentName, studentList, visit):
    dayList = []
    subDayList = []
    dayList.append(studentName)
    visit[studentName] = 1
    remove = 0;
    tempremove = 0;
    # add the initial list of friends
    for friends in studentList[studentName]:
        subDayList.append(friends)
        visit[friends] = 1
        remove += 1
    subDayList.sort()
    # add the next day of vertices
    while remove > 0:
        name = subDayList.pop(0)
        dayList.append(name)
        remove -= 1
        for toldRumor in studentList[name]:
            if visit[toldRumor] is 0:
                subDayList.append(toldRumor)
                visit[toldRumor] = 1
                tempremove += 1
        if remove is 0:
            remove = tempremove
            tempremove = 0;
            subDayList.sort()
    for student, wasVisited in visit.items():
        if wasVisited == 0:
            subDayList.append(student)
    if len(subDayList) > 0:
        subDayList.sort()
        for untold in subDayList:
            dayList.append(untold)
    for students in dayList:
        print(students, end=" ")

def main():
    students = {}
    visited = {}
    namesTotal = int(input())
    i = 0
    while i < namesTotal:
        name = input()
        students[name] = []
        visited[name] = 0
        i = i + 1
    friendsTotal = int(input())
    j = 0
    while j < friendsTotal:
        friend1, friend2 = input().split(" ")
        if friend2 not in students[friend1]:
            students[friend1].append(friend2)
        if friend1 not in students[friend2]:
            students[friend2].append(friend1)
        j = j + 1
    rumorsTotal = int(input())
    x = 0
    while x < rumorsTotal:
        visitedCopy = visited.copy()
        starter = input()
        rumorReport(starter, students, visitedCopy)
        x += 1


if __name__ == "__main__":
    main()
