exam_counts = {}
for exam in exams_cal.events:
    exam_date_str = exam.begin.strftime('%Y-%m-%d')
    exam_counts[exam_date_str] = exam_counts.get(exam_date_str, 0) + 1
    
exam_counts = pd.DataFrame.from_dict({ 'date': list(exam_counts.keys()), 'num': list(exam_counts.values()) })
exam_counts['date']  = pd.to_datetime(exam_counts['date'])