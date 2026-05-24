Payload /api/v1/predict
```json
{
  "cv_text": "Experienced Senior Software Engineer with 6+ years of expertise in building scalable web applications using Python, Django, and React.js. Proven track record in designing RESTful APIs, optimizing PostgreSQL databases, and implementing CI/CD pipelines with Docker and Kubernetes. Strong background in cloud infrastructure on AWS (EC2, S3, Lambda). Skilled in agile methodologies, cross-functional team collaboration, and mentoring junior developers. Passionate about clean code, test-driven development, and solving complex technical challenges.",
  "job_description": "Senior Backend Engineer: We are looking for an experienced Python developer to build high-performance microservices. Requirements include 5+ years of experience with Django or FastAPI, strong knowledge of SQL databases, and experience with AWS cloud services. You will be responsible for API design, system architecture, and ensuring scalability.",
  "user_id": "user_123"
}
```

Response /api/v1/predict
```json
{
  "matching_score": 0.7288,
  "confidence": "High",
  "recommendation": "Highly Recommended",
  "inference_time_ms": 119.7
}
```

====================

Payload /api/v1/predict/batch
```json
{
  "cv_text": "Frontend Developer with 2.5 years of experience building responsive and performant web applications. Skilled in React.js, Next.js, TypeScript, and Tailwind CSS. Implemented component libraries and state management using Redux Toolkit and Zustand. Experience with unit testing using Jest and React Testing Library. Optimized web performance, achieving 90+ Lighthouse scores across all metrics. Integrated RESTful APIs and GraphQL (Apollo Client). Familiar with version control using Git and collaborative workflows (code reviews, agile ceremonies). Eager to learn and stay updated with modern frontend trends. Previously contributed to an e-commerce platform used by 50k+ monthly active users. Strong attention to UI/UX details and accessibility standards (WCAG 2.1).",
  "job_descriptions": [
    "Looking for Frontend Engineer with 1-3 years experience in React.js and TypeScript. Must have strong understanding of component-based architecture, state management (Redux/Zustand), and responsive design. Familiarity with RESTful API integration and Git workflows required.",
    "Seeking entry-level Frontend Developer proficient in HTML5, CSS3, and JavaScript (ES6). Experience with React or Vue.js is a plus. Willingness to learn, good communication skills, and basic knowledge of version control (Git) are essential.",
    "Mid-level Frontend Engineer needed with 2-4 years experience in Next.js and Tailwind CSS. Should have experience optimizing web performance (Lighthouse scores 90+), implementing unit tests (Jest/React Testing Library), and collaborating with designers via Figma.",
    "Looking for Frontend Developer skilled in building responsive web applications using modern frameworks (React/Angular). Must understand accessibility standards (WCAG 2.1), cross-browser compatibility, and basic SEO principles. Experience with Webpack/Vite is a plus.",
    "Seeking React specialist with 2+ years experience in building reusable component libraries. Must have strong knowledge of hooks, custom hooks, and context API. Familiarity with GraphQL (Apollo Client) and Tailwind CSS preferred. Opportunity to mentor interns.",
    "DevOps Engineer: Responsible for maintaining and improving our cloud infrastructure on AWS. Expertise in Kubernetes, Terraform, and CI/CD tools (Jenkins/GitLab CI) is essential. You will automate deployment processes and monitor system performance.",
    "Data Engineer: Build and maintain data pipelines for large-scale datasets. Requires strong skills in Python, SQL, Apache Spark, and Airflow. Experience with data warehousing solutions like Snowflake or Redshift is a plus.",
    "Machine Learning Engineer: Develop and deploy NLP models for production environments. PhD or Masters in Computer Science preferred. Must have experience with PyTorch or TensorFlow, and familiarity with MLOps practices.",
    "Mobile Developer (iOS/Android): Create native mobile applications using Swift or Kotlin. 3+ years of experience in mobile development, including publishing apps to App Store/Play Store. Knowledge of cross-platform frameworks like Flutter is beneficial.",
    "Cloud Solutions Architect: Design secure and scalable cloud architectures for enterprise clients. AWS Certified Solutions Architect certification required. Deep understanding of networking, security groups, and serverless computing.",
    "Engineering Team Lead: Lead a squad of 5-7 engineers in delivering high-quality software products. Requires strong technical background in web development plus excellent leadership and communication skills. Experience in agile project management is mandatory."
  ],
  "user_id": "candidate_123"
}
```

Response /api/v1/predict/batch
```json
{
  "results": [
    {
      "rank": 1,
      "job_index": 0,
      "matching_score": 0.8611,
      "confidence": "High",
      "recommendation": "Highly Recommended",
      "inference_time_ms": 79.18
    },
    {
      "rank": 2,
      "job_index": 2,
      "matching_score": 0.8136,
      "confidence": "High",
      "recommendation": "Highly Recommended",
      "inference_time_ms": 79.18
    },
    {
      "rank": 3,
      "job_index": 1,
      "matching_score": 0.7119,
      "confidence": "High",
      "recommendation": "Highly Recommended",
      "inference_time_ms": 79.18
    },
    {
      "rank": 4,
      "job_index": 3,
      "matching_score": 0.6704,
      "confidence": "Medium",
      "recommendation": "Consider",
      "inference_time_ms": 79.18
    },
    {
      "rank": 5,
      "job_index": 8,
      "matching_score": 0.5325,
      "confidence": "Medium",
      "recommendation": "Consider",
      "inference_time_ms": 79.18
    },
    {
      "rank": 6,
      "job_index": 4,
      "matching_score": 0.4508,
      "confidence": "Medium",
      "recommendation": "Consider",
      "inference_time_ms": 79.18
    },
    {
      "rank": 7,
      "job_index": 10,
      "matching_score": 0.2363,
      "confidence": "Low",
      "recommendation": "Not Recommended",
      "inference_time_ms": 79.18
    },
    {
      "rank": 8,
      "job_index": 6,
      "matching_score": 0.1665,
      "confidence": "Low",
      "recommendation": "Not Recommended",
      "inference_time_ms": 79.18
    },
    {
      "rank": 9,
      "job_index": 9,
      "matching_score": 0.1579,
      "confidence": "Low",
      "recommendation": "Not Recommended",
      "inference_time_ms": 79.18
    },
    {
      "rank": 10,
      "job_index": 5,
      "matching_score": 0.1561,
      "confidence": "Low",
      "recommendation": "Not Recommended",
      "inference_time_ms": 79.18
    },
    {
      "rank": 11,
      "job_index": 7,
      "matching_score": 0.1341,
      "confidence": "Low",
      "recommendation": "Not Recommended",
      "inference_time_ms": 79.18
    }
  ],
  "total_items": 11,
  "total_time_ms": 870.98
}
```

====================

Payload /api/v1/skill-gap 
```json
{
    "cv_text": "Experienced Senior Software Engineer with 6+ years of expertise in building scalable web applications using Python, Django, and React.js. Proven track record in designing RESTful APIs, optimizing PostgreSQL databases, and implementing CI/CD pipelines with Docker and Kubernetes. Strong background in cloud infrastructure on AWS (EC2, S3, Lambda). Skilled in agile methodologies, cross-functional team collaboration, and mentoring junior developers. Passionate about clean code, test-driven development, and solving complex technical challenges.",
    "job_description": "Senior Backend Engineer: We are looking for an experienced Python developer to build high-performance microservices. Requirements include 5+ years of experience with Django or FastAPI, strong knowledge of SQL databases, and experience with AWS cloud services. You will be responsible for API design, system architecture, and ensuring scalability."
}
```

Response /api/v1/skill-gap
```json
{
  "skill_gap_score": 0.375,
  "skill_coverage_percent": "37%",
  "top_priority_skill": "api design",
  "present_skills": [
    {
      "skill": "python",
      "skill_id": "KS125LS6N7WP4S6SFTCK",
      "match_score": 1,
      "priority": 0
    },
    {
      "skill": "django",
      "skill_id": "KS1232D6PH6SBVWWPQWC",
      "match_score": 1,
      "priority": 0
    },
    {
      "skill": "cloud service",
      "skill_id": "ES43DB1E2DEC412F3A26",
      "match_score": 0.7961,
      "priority": 0
    }
  ],
  "missing_skills": [
    {
      "skill": "api design",
      "skill_id": "KSS344MJ1FTC11D417OQ",
      "match_score": 0,
      "priority": 1
    },
    {
      "skill": "system architecture",
      "skill_id": "KS441536VTGSWK6MDLMT",
      "match_score": 0,
      "priority": 2
    },
    {
      "skill": "backend",
      "skill_id": "KS7R8G2D52QH187SED9R",
      "match_score": 0,
      "priority": 3
    },
    {
      "skill": "microservices",
      "skill_id": "KSZX7YZWNR5IDR1I2VMZ",
      "match_score": 0,
      "priority": 4
    },
    {
      "skill": "scalability",
      "skill_id": "KS124RX787SQ1WVD8XF6",
      "match_score": 0,
      "priority": 5
    }
  ],
  "recommendation_summary": "Kesesuaian skill: 37% (perlu peningkatan). Skill yang sudah dimiliki: python, django, cloud service. Prioritaskan mempelajari: api design, system architecture, backend.",
  "analysis_time_ms": 13485.63
}
```

====================

Payload /api/v1/extract-cv-skills
```json
{
  "cv_text": "Frontend Developer with 2.5 years of experience building responsive and performant web applications. Skilled in React.js, Next.js, TypeScript, and Tailwind CSS. Implemented component libraries and state management using Redux Toolkit and Zustand. Experience with unit testing using Jest and React Testing Library. Optimized web performance, achieving 90+ Lighthouse scores across all metrics. Integrated RESTful APIs and GraphQL (Apollo Client). Familiar with version control using Git and collaborative workflows (code reviews, agile ceremonies). Eager to learn and stay updated with modern frontend trends. Previously contributed to an e-commerce platform used by 50k+ monthly active users. Strong attention to UI/UX details and accessibility standards (WCAG 2.1)."
}
```

Response /api/v1/extract-cv-skills
```json
{
  "skills": [
    {
      "skill": "restful apis",
      "skill_id": "KS4401V5WX78L6JX0NW7",
      "confidence": 2
    },
    {
      "skill": "graphql apollo",
      "skill_id": "ESED2F04B4C8848FB59C",
      "confidence": 2
    },
    {
      "skill": "web application",
      "skill_id": "KS441ZY6P0PDB5DWTRB8",
      "confidence": 1
    },
    {
      "skill": "react js",
      "skill_id": "KSDJCA4E89LB98JAZ7LZ",
      "confidence": 1
    },
    {
      "skill": "next js",
      "skill_id": "ES7CA4F00390885DBAAB",
      "confidence": 1
    },
    {
      "skill": "unit testing",
      "skill_id": "KS120SX72T8B5VLXS1VN",
      "confidence": 1
    },
    {
      "skill": "version control",
      "skill_id": "KS1222C6WKYWRKRXQCR0",
      "confidence": 1
    },
    {
      "skill": "code review",
      "skill_id": "KS1222G6RD9GBB7Q6FY5",
      "confidence": 1
    },
    {
      "skill": "e commerce",
      "skill_id": "KS1238H659P08Z726BK8",
      "confidence": 1
    },
    {
      "skill": "css",
      "skill_id": "KS121F45VPV8C9W3QFYH",
      "confidence": 1
    },
    {
      "skill": "typescript",
      "skill_id": "KS441LF7187KS0CV4B6Y",
      "confidence": 1
    },
    {
      "skill": "management",
      "skill_id": "KS1218W78FGVPVP2KXPX",
      "confidence": 1
    },
    {
      "skill": "redux",
      "skill_id": "KSQOOX1S2DYD0E1VVZ5X",
      "confidence": 1
    },
    {
      "skill": "jest",
      "skill_id": "ES69297559170A17D44A",
      "confidence": 1
    },
    {
      "skill": "library",
      "skill_id": "KS122086PPY11B2M1G6N",
      "confidence": 1
    },
    {
      "skill": "git",
      "skill_id": "ESA91D8112EB9ECA3570",
      "confidence": 1
    },
    {
      "skill": "workflows",
      "skill_id": "KS4424T6KPTTQ1NKM0XK",
      "confidence": 1
    }
  ],
  "skill_names": [
    "restful apis",
    "graphql apollo",
    "web application",
    "react js",
    "next js",
    "unit testing",
    "version control",
    "code review",
    "e commerce",
    "css",
    "typescript",
    "management",
    "redux",
    "jest",
    "library",
    "git",
    "workflows"
  ],
  "total_skills": 17,
  "extraction_time_ms": 425.39
}
```

====================

Payload /api/v1/analyze-cv
```json
{
  "cv_text": "Senior Backend Engineer with 7+ years of experience in building scalable distributed systems. Currently at PT Teknologi Nusantara (2021–present), leading 3 engineers in developing microservices handling 10k+ RPS.\n\nEDUCATION:\n- Master of Computer Science, Universitas Indonesia (2020), GPA 3.85/4.00\n- Bachelor of Informatics, ITB (2017), GPA 3.78/4.00\n\nPROJECTS:\n- Payment Gateway System: Designed idempotent transaction processing serving 500k+ users/month using Python, FastAPI, and PostgreSQL\n- Real-time Notification Engine: Built WebSocket-based notification system handling 50k concurrent connections with Redis Pub/Sub\n- API Rate Limiter: Implemented distributed rate limiting using Redis + Lua scripts for 10+ internal services\n\nORGANIZATIONS:\n- Python Indonesia Community (Core Contributor, 2022–present): Organized 5 nationwide meetups\n- GDG Jakarta (Co-Organizer, 2021–2023): Managed speaker sessions for 500+ participants\n\nCERTIFICATIONS:\n- AWS Solutions Architect – Associate (2023)\n- MongoDB Certified Developer (2022)\n\nACHIEVEMENTS:\n- Best Innovation Award at Company Hackathon 2023\n- Reduced API latency by 40% (Team achievement, Q4 2022)\n\nTECH STACK: Python, FastAPI, Django, PostgreSQL, Redis, RabbitMQ, Docker, Kubernetes, AWS (EC2, RDS, ElastiCache)",
  "top_n_titles": 5
}
```

Response /api/v1/analyze-cv
```json
{
  "current_role": "Senior Backend Developer",
  "experience": "7+ Years",
  "education": "Master Computer Science",
  "extracted_skills": [
    "aws",
    "distributed_systems",
    "docker",
    "kubernetes",
    "mongodb",
    "postgresql",
    "python",
    "redis"
  ],
  "suggested_job_titles": [
    {
      "title": "Architect / Urban Planner",
      "role_key": "architect_design",
      "confidence": 1,
      "reason": "Detected as current role in CV",
      "matched_skills": []
    },
    {
      "title": "Data Engineer",
      "role_key": "data_engineer",
      "confidence": 0.25,
      "reason": "6 matching skills: aws, distributed_systems, docker, mongodb and 2 more",
      "matched_skills": [
        "aws",
        "distributed_systems",
        "docker",
        "mongodb",
        "postgresql",
        "python"
      ]
    },
    {
      "title": "DevOps Engineer",
      "role_key": "devops",
      "confidence": 0.2,
      "reason": "4 matching skills: aws, docker, kubernetes, python",
      "matched_skills": [
        "aws",
        "docker",
        "kubernetes",
        "python"
      ]
    }
  ],
  "analysis_time_ms": 21.42
}
```

====================

Payload /api/v1/recommend
```json
{
  "cv_text": "Frontend Developer with 2.5 years of experience building responsive and performant web applications. Skilled in React.js, Next.js, TypeScript, and Tailwind CSS. Implemented component libraries and state management using Redux Toolkit and Zustand. Experience with unit testing using Jest and React Testing Library. Optimized web performance, achieving 90+ Lighthouse scores across all metrics. Integrated RESTful APIs and GraphQL (Apollo Client). Familiar with version control using Git and collaborative workflows (code reviews, agile ceremonies). Eager to learn and stay updated with modern frontend trends. Previously contributed to an e-commerce platform used by 50k+ monthly active users. Strong attention to UI/UX details and accessibility standards (WCAG 2.1).",
  "job_postings": [
    {
      "job_id": "job_001",
      "job_title": "Frontend Engineer",
      "job_description": "Looking for Frontend Engineer with 1-3 years experience in React.js and TypeScript. Must have strong understanding of component-based architecture, state management (Redux/Zustand), and responsive design. Familiarity with RESTful API integration and Git workflows required."
    },
    {
      "job_id": "job_002",
      "job_title": "Junior Frontend Developer",
      "job_description": "Seeking entry-level Frontend Developer proficient in HTML5, CSS3, and JavaScript (ES6). Experience with React or Vue.js is a plus. Willingness to learn, good communication skills, and basic knowledge of version control (Git) are essential."
    },
    {
      "job_id": "job_003",
      "job_title": "Mid-Level UI Engineer",
      "job_description": "Mid-level Frontend Engineer needed with 2-4 years experience in Next.js and Tailwind CSS. Should have experience optimizing web performance (Lighthouse scores 90+), implementing unit tests (Jest/React Testing Library), and collaborating with designers via Figma."
    },
    {
      "job_id": "job_004",
      "job_title": "Frontend Web Developer",
      "job_description": "Looking for Frontend Developer skilled in building responsive web applications using modern frameworks (React/Angular). Must understand accessibility standards (WCAG 2.1), cross-browser compatibility, and basic SEO principles. Experience with Webpack/Vite is a plus."
    },
    {
      "job_id": "job_005",
      "job_title": "UI Developer (React Specialist)",
      "job_description": "Seeking React specialist with 2+ years experience in building reusable component libraries. Must have strong knowledge of hooks, custom hooks, and context API. Familiarity with GraphQL (Apollo Client) and Tailwind CSS preferred. Opportunity to mentor interns."
    }
  ],
  "job_title": "Frontend Engineer"
}
```

Response /api/v1/recommend
```json
{
  "job_title_selected": "Frontend Engineer",
  "results": [
    {
      "rank": 1,
      "job_id": "job_001",
      "job_title": "Frontend Engineer",
      "matching_score": 0.8611,
      "confidence": "High",
      "recommendation": "Highly Recommended",
      "raw_model_score": 0.7537,
      "structured_score": 0.88,
      "inference_time_ms": 75.02
    },
    {
      "rank": 2,
      "job_id": "job_003",
      "job_title": "Mid-Level UI Engineer",
      "matching_score": 0.8136,
      "confidence": "High",
      "recommendation": "Highly Recommended",
      "raw_model_score": 0.7961,
      "structured_score": 0.8167,
      "inference_time_ms": 75.02
    },
    {
      "rank": 3,
      "job_id": "job_002",
      "job_title": "Junior Frontend Developer",
      "matching_score": 0.7119,
      "confidence": "High",
      "recommendation": "Highly Recommended",
      "raw_model_score": 0.7374,
      "structured_score": 0.695,
      "inference_time_ms": 75.02
    },
    {
      "rank": 4,
      "job_id": "job_004",
      "job_title": "Frontend Web Developer",
      "matching_score": 0.6704,
      "confidence": "Medium",
      "recommendation": "Consider",
      "raw_model_score": 0.7261,
      "structured_score": 0.6333,
      "inference_time_ms": 75.02
    },
    {
      "rank": 5,
      "job_id": "job_005",
      "job_title": "UI Developer (React Specialist)",
      "matching_score": 0.4508,
      "confidence": "Medium",
      "recommendation": "Consider",
      "raw_model_score": 0.7234,
      "structured_score": 0.2691,
      "inference_time_ms": 75.02
    }
  ],
  "total_items": 5,
  "total_time_ms": 457.39,
  "industry_skill_analysis": {
    "core": {
      "required": [
        "react",
        "html_css"
      ],
      "matched": [
        "html_css",
        "react"
      ],
      "missing": [],
      "readiness_pct": 100
    },
    "common": {
      "required": [
        "typescript",
        "javascript",
        "vue",
        "figma",
        "seo",
        "angular",
        "graphql"
      ],
      "matched": [
        "graphql",
        "typescript"
      ],
      "missing": [
        "angular",
        "figma",
        "javascript",
        "seo",
        "vue"
      ],
      "readiness_pct": 28.6
    },
    "optional": [],
    "readiness_percentage": 78.6,
    "readiness_label": "Almost Ready",
    "priority_gaps": [
      {
        "skill": "angular",
        "frequency": 0.2,
        "tier": "common"
      },
      {
        "skill": "figma",
        "frequency": 0.2,
        "tier": "common"
      },
      {
        "skill": "javascript",
        "frequency": 0.2,
        "tier": "common"
      },
      {
        "skill": "seo",
        "frequency": 0.2,
        "tier": "common"
      },
      {
        "skill": "vue",
        "frequency": 0.2,
        "tier": "common"
      }
    ],
    "bonus_skills": [
      "agile",
      "design_general"
    ],
    "postings_analyzed": 5,
    "skill_frequency": {
      "typescript": 0.2,
      "react": 1,
      "javascript": 0.2,
      "vue": 0.2,
      "html_css": 0.6,
      "figma": 0.2,
      "seo": 0.2,
      "angular": 0.2,
      "graphql": 0.2
    },
    "high_diversity": true,
    "effective_thresholds": {
      "core": 0.4,
      "common": 0.2
    }
  }
}
```