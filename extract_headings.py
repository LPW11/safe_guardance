import re

# 读取Markdown文件
with open('视频侦查技术.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义标题正则表达式
# 匹配一级标题: # 标题
level1_pattern = r'^#\s+(.+)$'
# 匹配二级标题: ## 标题
level2_pattern = r'^##\s+(.+)$'
# 匹配三级标题: ### 标题
level3_pattern = r'^###\s+(.+)$'
# 匹配四级标题: #### 标题
level4_pattern = r'^####\s+(.+)$'

# 提取标题
headings = []
lines = content.split('\n')

for line in lines:
    line = line.strip()
    # 匹配一级标题
    match1 = re.match(level1_pattern, line)
    if match1:
        headings.append({"level": 1, "title": match1.group(1)})
        continue
    # 匹配二级标题
    match2 = re.match(level2_pattern, line)
    if match2:
        headings.append({"level": 2, "title": match2.group(1)})
        continue
    # 匹配三级标题
    match3 = re.match(level3_pattern, line)
    if match3:
        headings.append({"level": 3, "title": match3.group(1)})
        continue
    # 匹配四级标题
    match4 = re.match(level4_pattern, line)
    if match4:
        headings.append({"level": 4, "title": match4.group(1)})
        continue

# 生成Markdown格式的标题结构
markdown_output = "# 视频侦查技术 - 章节结构\n\n"

for heading in headings:
    if heading["level"] == 1:
        markdown_output += f"# {heading['title']}\n\n"
    elif heading["level"] == 2:
        markdown_output += f"## {heading['title']}\n\n"
    elif heading["level"] == 3:
        markdown_output += f"### {heading['title']}\n\n"
    elif heading["level"] == 4:
        markdown_output += f"#### {heading['title']}\n\n"

# 保存结果
with open('视频侦查技术_章节结构.md', 'w', encoding='utf-8') as f:
    f.write(markdown_output)

print("章节结构提取完成，保存到 '视频侦查技术_章节结构.md'")
print("\n提取的标题数量:")
print(f"- 一级标题: {sum(1 for h in headings if h['level'] == 1)}")
print(f"- 二级标题: {sum(1 for h in headings if h['level'] == 2)}")
print(f"- 三级标题: {sum(1 for h in headings if h['level'] == 3)}")
print(f"- 四级标题: {sum(1 for h in headings if h['level'] == 4)}")
