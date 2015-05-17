# condense meeting times (combine overlaps)
# meeting_times is list of tuples

def condense_meeting_times(meeting_times) :
	sortedTimes = sorted(meeting_times)
	oldStart, oldEnd = sortedTimes[0]
	condensedTimes = []

	for newStart, newEnd in sortedTimes[1:] :
		if newStart <= oldEnd :
			oldEnd = max(oldEnd, newEnd)
		else :
			condensedTimes.append((oldStart, oldEnd))
			oldStart, oldEnd = newStart, newEnd
	condensedTimes.append((oldStart, oldEnd))
	return condensedTimes

print condense_meeting_times([(1,2), (2,3)])
print condense_meeting_times([(0,1), (3,5), (4,8), (10,12), (9,10)])
print condense_meeting_times([(1,5), (2,3)])
print condense_meeting_times([(1,10), (2,6), (3,5), (7,9)])