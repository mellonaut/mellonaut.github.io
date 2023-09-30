class BlogPost:
    def __init__(self, id, title, date, header, sections, image, clip_path, email, certifications, github_link):
        self.id = id
        self.title = title
        self.date = date
        self.header = header
        self.sections = sections
        self.image = image
        self.clip_path = clip_path
        self.email = email
        self.certifications = certifications
        self.github_link = github_link

    def generate_description(self):
        content = [f"<h1>{self.header}</h1>"]
        for section in self.sections:
            content.append(f"<p>{section}</p>")
        
        if self.image:
            content.append(f"<img class='post-article__image' src='{self.image}' alt='Description of the image'>")
        
        if self.github_link:
            content.append(f"<h3>Github</h3><p><a href='{self.github_link}'>Coding Projects</a></p>")
        
        if self.certifications:
            content.append("<h3>Certifications:</h3>")
            for cert in self.certifications:
                content.append(f"<p><a href='{cert['link']}'>{cert['name']}</a></p>")
        
        if self.email:
            content.append(f"<p>Email: <a href='mailto:{self.email}'>{self.email}</a></p>")

        return ''.join(content)

    def generate_block(self):
        description_content = self.generate_description()
        block = f"""
{{
    id: {self.id},
    title: "{self.title}",
    date: "{self.date}",
    description: "{description_content}",
    image: "{self.image}",
    clip_path: "{self.clip_path}"
}}
        """
        return block


# Usage:
sections = [
    "Dev. Sec. Oops.",
    "A development blog, personal and technical, with a focus on Microsoft security and the Azure cloud. Purple Team Stories, demos, bad memes, and code review. This will will help track my progress, let me do in depth write-ups on some of the tools I've made over the last couple of years to help myself and share cheatsheets, code and techniques that have worked for me lately. So much of learning security is reading old blogs, and new blogs based on the old blogs. Maybe someone finds something in this useful."
]

certifications = [
    {"name": "(In progress) CRTO - Certified Red Team Operator", "link": "https://training.zeropointsecurity.co.uk/courses/red-team-ops"},
    # Add more certifications as needed
]

post = BlogPost(
    id=1,
    title="Straylight Blog: An Anthology of Failures",
    date="2023",
    header="Dev. Sec. Oops.",
    sections=sections,
    image="https://dev.straylightsecurity.com/assets/lich3.jpg",
    clip_path="polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)",
    email="mellonaut@straylightsecurity.com",
    certifications=certifications,
    github_link="https://github.com/mellosec"
)

print(post.generate_block())
