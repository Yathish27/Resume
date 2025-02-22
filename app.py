import streamlit as st

# Set up the page configuration
image_url = "https://raw.githubusercontent.com/Yathish27/Resume/refs/heads/main/IMG_1674.jpg"
url = str(image_url).strip()

st.set_page_config(page_title="Yathish Naraganahalli Veerabhadraiah - Portfolio", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
sections = ["Home", "Summary", "Experience", "Projects", "Education", "Skills"]
selected_section = st.sidebar.radio("Go to:", sections)

# Home Section
if selected_section == "Home":
    st.title("Yathish Naraganahalli Veerabhadraiah")
    st.markdown("""
    **Email:** yn2426@nyu.edu   
    **LinkedIn:** [linkedin.com/in/yathish-naraganahalli-veerabhadraiah24656b16a](https://linkedin.com/in/yathish-naraganahalli-veerabhadraiah24656b16a)  
    """)
    st.image(url, caption="Your Profile Picture", width=350)
    st.write("Welcome to my portfolio! Explore my professional journey, skills, and projects.")

# Summary Section
elif selected_section == "Summary":
    st.header("Summary")
    st.write("""
    I am currently pursuing a Master’s degree in Cybersecurity at New York University’s Tandon School of Engineering. My areas of specialization include Information Security, Network Security, Ethical Hacking, and AI for Cybersecurity. Before starting my academic journey at NYU, I worked as a DevOps Security Engineer at Schneider Electric in Bengaluru, India, for nearly two and a half years, including a six-month internship at the beginning of my career.

During my time at Schneider Electric, I developed expertise in DevSecOps release management using technologies such as GitHub Actions, Bitbucket, AWS, and Docker. I played a key role in the company’s migration to Enterprise Cloud, which resulted in significant cost savings. My responsibilities included hosting servers in Docker containers and integrating them with Salesforce Cloud. This was part of a broader initiative to enhance digital customer relationship management by integrating Salesforce with SAP and Schneider Product Information Management systems. I also collaborated with over 80 developers to manage critical Agile release cycles and contributed to several proof-of-concept projects. Notably, I explored Kubernetes as an orchestration manager and designed AI-driven solutions for creating product catalogs and brochures, which are planned for rollout in 2025.

Before joining Schneider Electric, I worked as a research intern at PES University during my undergraduate studies. There, I developed an “AI-based Modular Agriculture Robot” using 3D-printed components. The robot utilized Raspberry Pi for the web server and Arduino with sensors to control motion and collect data from agricultural fields. Its capabilities included crop and weed detection, fruit identification, and pest monitoring.

For my capstone project at NYU, I focused on deepfake detection. I developed a solution using state-of-the-art deep learning models such as EfficientNet B7, Xception Net, and Inception ResNet to learn facial characteristics. These models were integrated with LSTM neural networks to identify spatial inconsistencies in video frames. This project addressed the growing threat of deepfakes created by platforms like DeepSwap and DeepFace Labs that have been used to spread misinformation involving public figures such as Barack Obama and Donald Trump. My solution aimed to mitigate social abuse, political manipulation, and other harmful effects by providing highly accurate detection mechanisms. Additionally, I conducted a comparative study of various models, ensembled their results, and classified them effectively.

Beyond my academic and professional work, I have been actively involved in teaching AI and Robotics as a part-time tutor for undergraduate students. I focused on helping students understand practical approaches through real-world case studies. I am also an active member of the Cybersecurity Club, participate in CTF hackathons, and engage in bug bounty hunting.
    """)

# Experience Section
elif selected_section == "Experience":
    st.header("Experience")
    
    st.subheader("Founding Engineer | Plurall AI | New York | NYU Lesile Lab")
    st.write("""
    - **Duration:** October 2024 - January 2025  
    - Developed an AI-powered deepfake detection system to prevent impersonation and fraud by identifying spatial inconsistencies in AI-generated faces.
    """)
    
    st.subheader("Platform DevOps Engineer | Schneider Electric | Bengaluru")
    st.write("""
    - **Duration:** August 2022 - August 2024  
    - Managed DevSecOps release cycles integrated with Salesforce and GitHub pipelines.  
    - Monitored security using tools like Gitleaks and Tableau dashboards while maintaining cloud security.
    """)
    
    st.subheader("Part-time Academic Tutor and Mentor | IntrnForte | Bengaluru")
    st.write("""
    - **Duration:** November 2022 - August 2024  
    - Delivered over 20 hours of lectures on AI, Cybersecurity, and Robotics with hands-on sessions and industry-level projects.
    """)
    
    st.subheader("Robotics & AI Research Intern | PES University | Bengaluru")
    st.write("""
    - **Duration:** September 2021 - August 2022  
    - Designed intelligent modular robots for agricultural applications using ROS and deep learning models.
    """)

# Projects Section
elif selected_section == "Projects":
    st.header("Projects")
    
    st.subheader("Spybot | HackNYU Hackathon | February 2025")
    st.write("""
    Built an AI-powered phishing and spam detector that analyzes behavioral patterns and contextual cues in emails to identify threats.
    """)
    
    st.subheader("Deep Fake Detection System | PES University")
    st.write("""
    Developed a fake face detection system using computer vision and neural networks to identify facial inconsistencies.
    """)
    
    st.subheader("E-yantra Robotic Competition | IIT Bombay")
    st.write("""
    Simulated an automated warehouse system in a 3D Gazebo dynamic simulator for efficient order management.
    """)

# Education Section
elif selected_section == "Education":
    st.header("Education")
    
    st.subheader("Master's in Cybersecurity | New York University | GPA: 4.0/4.0")
    st.write("""
    - **Duration:** 2024-Present  
      Courses: Information Security & Privacy, Network Security, Computer Networking, Penetration Testing & Vulnerability Analysis.
      """)
      
    st.subheader("B.Tech in Computer Science Engineering | PES University | GPA: 7.86/10")
    st.write("""
      - **Duration:** 2018-2022  
      Focused on AI, Robotics, and Cybersecurity.
      """)

# Skills Section
elif selected_section == "Skills":
    st.header("Skills")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Technical Skills:")
        skills = [
            "Penetration Testing", "Network Security", "Cryptography",
            "Malware Analysis", "Cloud Security", "Application Security",
            "Bug Bounty Hunting", "Risk Analysis"
        ]
        for skill in skills:
            st.markdown(f"- {skill}")
            
        tools = [
            "Firewalls & IDS", "Burp Suite", "Postman",
            "OWASP Tools", "TryHackMe Labs", "PortSwigger Labs"
        ]
        st.subheader("Tools:")
        for tool in tools:
            st.markdown(f"- {tool}")
            
        
    
        
