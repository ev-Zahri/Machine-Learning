Payload /api/v1/skill-gap test case 1
```json
{
    "cv_text": "Experienced Senior Software Engineer with 6+ years of expertise in building scalable web applications using Python, Django, and React.js. Proven track record in designing RESTful APIs, optimizing PostgreSQL databases, and implementing CI/CD pipelines with Docker and Kubernetes. Strong background in cloud infrastructure on AWS (EC2, S3, Lambda). Skilled in agile methodologies, cross-functional team collaboration, and mentoring junior developers. Passionate about clean code, test-driven development, and solving complex technical challenges.",
    "job_description": "Senior Backend Engineer: We are looking for an experienced Python developer to build high-performance microservices. Requirements include 5+ years of experience with Django or FastAPI, strong knowledge of SQL databases, and experience with AWS cloud services. You will be responsible for API design, system architecture, and ensuring scalability."
}
```
Response /api/v1/skill-gap test case 1
```json
{
  "skill_gap_score": 0.3333,
  "skill_coverage_percent": "33%",
  "top_priority_skill": "api design",
  "present_skills": [
    {
      "skill": "aws cloud",
      "weight": 0.1271,
      "priority": 0
    },
    {
      "skill": "databases experience",
      "weight": 0.1271,
      "priority": 0
    },
    {
      "skill": "experience aws",
      "weight": 0.1271,
      "priority": 0
    },
    {
      "skill": "experience django",
      "weight": 0.1271,
      "priority": 0
    },
    {
      "skill": "experienced python",
      "weight": 0.1271,
      "priority": 0
    }
  ],
  "missing_skills": [
    {
      "skill": "api design",
      "weight": 0.1271,
      "priority": 1
    },
    {
      "skill": "architecture ensuring",
      "weight": 0.1271,
      "priority": 2
    },
    {
      "skill": "backend engineer",
      "weight": 0.1271,
      "priority": 3
    },
    {
      "skill": "build high",
      "weight": 0.1271,
      "priority": 4
    },
    {
      "skill": "cloud services",
      "weight": 0.1271,
      "priority": 5
    },
    {
      "skill": "design architecture",
      "weight": 0.1271,
      "priority": 6
    },
    {
      "skill": "developer build",
      "weight": 0.1271,
      "priority": 7
    },
    {
      "skill": "django fastapi",
      "weight": 0.1271,
      "priority": 8
    },
    {
      "skill": "ensuring scalability",
      "weight": 0.1271,
      "priority": 9
    },
    {
      "skill": "fastapi strong",
      "weight": 0.1271,
      "priority": 10
    }
  ],
  "recommendation_summary": "Kesesuaian skill: 33% (perlu peningkatan). Skill yang sudah dimiliki: aws cloud, databases experience, experience aws. Prioritaskan mempelajari: api design, architecture ensuring, backend engineer.",
  "analysis_time_ms": 2.52
}
```

Payload /api/v1/skill-gap test case 2
```json
{
    "cv_text": "Experienced Senior Software Engineer with 6+ years of expertise in building scalable web applications using Python, Django, and React.js. Proven track record in designing RESTful APIs, optimizing PostgreSQL databases, and implementing CI/CD pipelines with Docker and Kubernetes. Strong background in cloud infrastructure on AWS (EC2, S3, Lambda). Skilled in agile methodologies, cross-functional team collaboration, and mentoring junior developers. Passionate about clean code, test-driven development, and solving complex technical challenges.",
    "job_description": "Full Stack Engineer: Seeking a versatile developer comfortable with both backend (Python/Node.js) and frontend (React/Vue) technologies. You will work on end-to-end feature development, from database schema design to UI implementation. 4+ years of commercial experience preferred."
}
```

Response /api/v1/skill-gap test case 2
```json
{
  "skill_gap_score": 0.0667,
  "skill_coverage_percent": "6%",
  "top_priority_skill": "backend python",
  "present_skills": [
    {
      "skill": "python",
      "weight": 0.1363,
      "priority": 0
    }
  ],
  "missing_skills": [
    {
      "skill": "backend python",
      "weight": 0.1363,
      "priority": 1
    },
    {
      "skill": "comfortable backend",
      "weight": 0.1363,
      "priority": 2
    },
    {
      "skill": "database schema",
      "weight": 0.1363,
      "priority": 3
    },
    {
      "skill": "design ui",
      "weight": 0.1363,
      "priority": 4
    },
    {
      "skill": "development database",
      "weight": 0.1363,
      "priority": 5
    },
    {
      "skill": "frontend react",
      "weight": 0.1363,
      "priority": 6
    },
    {
      "skill": "nodejs frontend",
      "weight": 0.1363,
      "priority": 7
    },
    {
      "skill": "python nodejs",
      "weight": 0.1363,
      "priority": 8
    },
    {
      "skill": "react vue",
      "weight": 0.1363,
      "priority": 9
    },
    {
      "skill": "vue technologies",
      "weight": 0.1363,
      "priority": 10
    },
    {
      "skill": "backend",
      "weight": 0.1363,
      "priority": 11
    },
    {
      "skill": "database",
      "weight": 0.1363,
      "priority": 12
    },
    {
      "skill": "frontend",
      "weight": 0.1363,
      "priority": 13
    },
    {
      "skill": "nodejs",
      "weight": 0.1363,
      "priority": 14
    }
  ],
  "recommendation_summary": "Kesesuaian skill: 6% (sangat kurang sesuai). Skill yang sudah dimiliki: python. CV belum memenuhi requirement posisi ini. Mulai dari: backend python, comfortable backend, database schema.",
  "analysis_time_ms": 3.52
}
```