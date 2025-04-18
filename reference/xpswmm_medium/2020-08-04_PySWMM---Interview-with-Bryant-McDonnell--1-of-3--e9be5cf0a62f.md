# PySWMM : Interview with Bryant McDonnell (1 of 3)

I am a big fan of PySWMM, which brings SWMM5 to the python world, a key computing language that powers the most exciting technology…

---

### PySWMM : Interview with Bryant McDonnell (1 of 3)

![](images\1__k2hjOWviqs5dIOn35w0Xw.png)

I am a big fan of [PySWMM](https://github.com/OpenWaterAnalytics/pyswmm), which brings SWMM5 to the python world, a key computing language that powers the most exciting technology advancement in artificial intelligence, big data and cloud computing. The possibilities PySWMM created is simply beyond my imagination.

Many thanks to [Bob](https://www.linkedin.com/in/robertdickinson/), the guru of all things about SWMM. Bob helped setup my interview with Bryant McDonnell, the creator of PySWMM.

I found Bryant’s PySWMM story quite inspiring, as PySWMM evolves Bryant turned himself from an civil engineer into a hydroinformatics engineer, a title I never heard of. He is truly a pioneer riding the technological wave, and this interview gives us a glimpse what that future might look like, and possibly how we can also catch that wave.

I transcribed/edited the hour long Zoom interview on 5/13/2020 into 3 posts.

[Part 1: The conception of PySWMM](https://medium.com/p/e9be5cf0a62f)

[Part 2: The Evolution of PySWMM](https://medium.com/p/f5243a59de9b)

[Part 3: Advice and future of PySWMM](https://medium.com/p/4ec86cd5c2ef)

**Mel: Could you please tell us a little bit about yourself?**

**Bryant**: I am a senior manager of hydroinfomatics and process control at Xylem Inc. This is a new title for me. I am in charge of overseeing a team that uses digital solutions and decision science to provide operational recommendation tools for utilities. This includes collection systems, water distribution systems, and treatment plants. I live in Chicago. I am a rock climber and I am pilot.

**Mel: That’s cool. How did you get started with Python?**

**Bryant**: The progression of programming languages went from C++/Java in high school; a little bit of C++ in my undergrad; when I got to grad school my Master’s work was half computational, half lab work so we did everything in MATLAB. Then when I started working for the Metropolitan Sewer District of Greater Cincinnati there was another opportunity to learn another language. A friend in Chicago who works in computer vision suggested I check out Python.

After finishing grad school, I worked for MSDGC in their modeling team, which was a cool opportunity to see the model calibration and update processes, and all of the monotonous tasks that are associated with that. So, at that time I told myself I cannot imagine myself manually moving data from ArcGIS to the model for the rest of my life. Then started looking at opportunities to automate the process. And ArcPy really opens up a lot of things, so I started to write small tools using ArcPy to hack that backend of ArcGIS of our processes to convert GIS data into SWMM input files. That was kind of the genesis of the whole (PySWMM) project.

**Mel: So, when did you start the PySWMM project?**

**Bryant**: About a couple of years into while I was working for Cincinnati. I went to the Cincinnati water distribution system symposium about every 6 months. Really cool opportunities for people from the USEPA, University of Cincinnati, other people from local universities to give an update on the kind of research they are into. Then I got to talking to Michael Tryby, now a good friend of mine (at USEPA). That was around 2012–2013, I told Michael that I was really interested in writing a Python interface for the EPA SWMM because that will really automate a lot of the things I do. And we started tossing some ideas, and someone sent me a link to someone who wrote a wrapper for EPANET. So, we kind of looked at that for inspiration. That’s how we started. The codebases live in an open sourced ecosystem at Open Water Analytics GitHub page: (<https://github.com/OpenWaterAnalytics>).

**Mel: It sounds that you started the project to solve a particular problem you had at that time?**

**Bryant**: Yes, and it didn’t have a lot of power back then. We could get it to run simulations, extract results out in a very basic level. The project was idled for a couple of years when I switched job and did some consulting work. So, around 2016 I joined EmNet, now a part Xylem, and that’s when I added more features.

**Mel: Could you please talk more about what happened after you joined EmNet?**

**Bryant**: I joined EmNet because I was magnetized by the leadership there. Luis has some really exciting ideas and was pushing the envelope of the industry. The team saw the initial value of what PySWMM can do for different pieces of their workflow. We started strategizing to add more features into PySWMM. I remembered one day I added the entry point to change the pump settings when the simulation was running. We had a meeting and we were all having coffee, I turned my laptop around, and I said: “Luis, check this out,” and Luis said, “OK I can see a lot of value of this.”

Although our BLU-X stack is proprietary, we started to find opportunities to share our ideas with the community. It does a lot of the things for the company and it aligned with our vision of a future digital utility. Also, this project is a great place to find likeminded individuals. It also positions our team as leaders in the smart water space. So, we are happy to be a contributor of the project.

**Mel: So, I can see getting involved in a project like PySWMM might have some career benefits. Could you talk about it more?**

**Bryant**: We’ve hired through GitHub several times now. If I see an interesting pull request to this project (a pull request is a process where someone can post development code and solicit feedback for changes before the code is pulled in and staged for the next code release), I’ll be on the phone and ask who are you. What are your interests? And what direction do you want to take your career. We are aiming for hydroinfomatics engineers. The running joke we have is “we are software engineers who accidentally signed up for civil/environmental engineering.” The interdisciplinary skills are so valuable because they bring new perspectives on solving problems.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 4, 2020](https://medium.com/p/e9be5cf0a62f).

[Canonical link](https://medium.com/@mel-meng-pe/pyswmm-interview-with-bryant-mcdonnell-1-of-3-e9be5cf0a62f)

Exported from [Medium](https://medium.com) on March 18, 2025.