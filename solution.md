# Part 1 — GyanBot System Prompt

**System Prompt**

**Identity:** You are **GyanBot**, an AI academic and career assistant for Indian engineering college students. You help students solve academic doubts, discover career paths, identify skill gaps, and find relevant events such as hackathons, workshops, and college fests.

**Tone:** Communicate in a calm, supportive, student-friendly way. Use simple explanations, relatable examples, and avoid intimidating jargon. Assume students may be stressed, confused, or under deadline pressure.

**Boundaries:**

1. Never generate fake internship openings, fake event dates, or invented college information.
2. Never provide harmful, illegal, or cheating-related content such as exam malpractice, plagiarism, or hacking instructions.
3. Do not give medical, legal, or financial advice beyond basic informational guidance.

**Format:** Structure every response into short sections with headings and bullet points. End with a clear “Next Steps” section.

**Scope:** In-scope topics include engineering academics, coding, project guidance, career planning, internships, skill development, and student events in India. Out-of-scope topics include political persuasion, personal therapy, relationship advice, and unrelated entertainment gossip.

**Why this boundary matters:**
The “no fake internships or event information” rule is critical because students may make real career decisions based on GyanBot’s answers. Hallucinated opportunities would reduce trust and could damage CampusConnect’s credibility among colleges and students.

---

# Part 2 — User Prompt Using C-I-F-C

### Prompt

**Context:**
I am Aryan, a 3rd-year Computer Science engineering student from Pune. I know Python, basic machine learning, pandas, and SQL fundamentals. I also have strong communication skills from participating in college presentations and group discussions. I want to secure a data science internship before December, but I am confused about which skills companies actually expect from interns and which companies I should target as a fresher.

**Instruction:**
Analyze my current profile, identify my missing skills, suggest a practical roadmap for the next 5 months, and recommend internship roles and companies suitable for my level.

**Format:**
Give the answer in these sections:

1. Current Strengths
2. Skill Gaps
3. Monthly Roadmap
4. Recommended Companies
5. Portfolio Projects
6. Next Steps

**Constraints:**
Keep the advice beginner-friendly, focused on Indian internship hiring trends, and avoid suggesting expensive paid courses.

---

# Part 3 — Recommended Framework and Justification

I would recommend **LangChain** for GyanBot.

LangChain is the best fit because GyanBot mainly needs a **single-agent workflow** with strong retrieval capabilities from syllabus PDFs, college FAQs, and career resources. LangChain’s Retrieval-Augmented Generation (RAG) pipelines, document loaders, vector database integrations, and prompt chaining make it ideal for combining LLM reasoning with institutional knowledge. It also supports structured prompting and tool calling while keeping responses fast and linear.

**CrewAI** is less suitable because it is designed for **multi-agent collaboration**, where different agents debate or divide tasks. GyanBot does not require separate specialist agents for this phase.

**AutoGen** is also less appropriate because it focuses heavily on autonomous multi-agent conversations and iterative interactions between agents, which can increase latency and complexity. CampusConnect instead needs predictable, fast, single-response outputs for students asking quick academic or career questions.

---

# Part 4 — Agent Flow for Career Guidance Feature

### Step 1 — Input (Prompt)

The student enters details such as branch, year, skills, interests, preferred career path, and target timeline.
Example: “I am a 3rd-year IT student with Python and SQL skills aiming for a data analyst internship.”

### Step 2 — Brain (System Prompt Activation)

The LLM receives GyanBot’s system prompt, which sets its role as a supportive engineering career assistant and defines formatting rules and boundaries.

### Step 3 — Brain (Intent & Profile Analysis)

The LLM analyzes the student’s profile to identify:

* Existing strengths
* Missing industry skills
* Career intent
* Urgency level

### Step 4 — Hands (Tool Call)

GyanBot queries the career resource database and vector store containing:

* Internship role requirements
* Resume guidelines
* Skill-roadmap documents
* Company hiring patterns
* Previous student placement insights

The tool fetches matching career paths, required skills, and internship recommendations relevant to the student profile.

### Step 5 — Brain (Reasoning & Personalization)

The LLM combines retrieved data with reasoning to create a personalized roadmap. It prioritizes beginner-friendly and realistic recommendations for Indian engineering students.

### Step 6 — Output (Result)

The student receives a structured response containing:

* Strengths summary
* Skill gaps
* Recommended tools/frameworks
* Monthly preparation roadmap
* Suggested companies and internship roles
* Portfolio project ideas
* “Next Steps” action checklist

The final output appears as clean headings with bullet points and short explanations for easy reading on mobile devices.
