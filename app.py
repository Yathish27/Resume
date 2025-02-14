import streamlit as st

# Set up the page configuration
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
    **Phone:** 347-466-6215  
    **LinkedIn:** [linkedin.com/in/yathish-naraganahalli-veerabhadraiah24656b16a](https://linkedin.com/in/yathish-naraganahalli-veerabhadraiah24656b16a)  
    """)
    st.image("https://drive.google.com/file/d/1cQCMHclZ3FHd4vCfAT0dxpMvkRP5dNx8/view?usp=sharing", caption="Your Profile Picture", width=150)
    st.write("Welcome to my portfolio! Explore my professional journey, skills, and projects.")

# Summary Section
elif selected_section == "Summary":
    st.header("Summary")
    st.write("""
    I am a Mastes student in Cybersecurity at New York University with expertise in Penetration Testing, Malware Analysis, Software Security, and Network Security. 
    With 2 years of experience as a DevSecOps Engineer at Schneider Electric, I have honed my skills in release management, Salesforce-GitHub integration, and cloud security.
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
            
        
    
        
