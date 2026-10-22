def parse_student(line):
    line = line.strip()
    if not line:
        raise ValueError("空行")
    parts = line.split(",")
    if len(parts)!=2:
        raise ValueError("字段数量不对")
    name, score_str = parts
    name = name.strip()
    if len(name)==0:
        raise ValueError("姓名为空")
    score = int(score_str.strip())
    if not (0<=score<=100):
        raise ValueError(f"成绩{score}超出0~100")
    return {"name":name, "score":score}
