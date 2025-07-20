---
title: Teaching coding in the midst of generative AI
date: 2024-08-20
---

I wrote the first half of what follows--my perspectives--before I did any systematic reading. I wanted to capture my state of mind as a teacher and programmer who is skeptical of generative artificial intelligence (GAI), because I was curious if that perspective would change.

Then I read fifteen recent studies, perspectives, and reviews to understand how coding educators are responding to the rise of ChatGPT, Copilot, and other GAI tools.

I tried to draw out the salient findings that came up across the literature about the effects, benefits, and risks, as well as the most convincing concrete recommendations for effective teaching.

I did not use GAI to research or write this piece, though I cannot be sure of my sources’ methods.

## My perspective as a language teacher

I discovered in early 2023 that many of the assignments I gave in my web development course could be completed by copy-pasting my instructions into ChatGPT.

This was annoying, but not particularly surprising, because these assignments are meant to be crystal clear and highly achievable if you are in the middle of learning a particular coding pattern. In fact I have always made it a point to write clear and concrete instructions for students, especially when I wanted to them to practice particular coding patterns they had just learned.

I have good pedagogical reasons for this, drawing on what I know about teaching modern foreign languages. In that context, you cultivate fluency by sequencing instruction in discrete pieces of the language that build on each other. Language is acquired by combining knowledge about the thing--vocabulary and grammar--with practice doing the thing--situational conversations with other students, real-life scenarios, and goal-oriented writing assignments. This graded blend of theory and practice is crucial to being able to speak and write more fluently over time.

Applying this method to teaching programming, I aim to have students practice the thing they learned that day. I do not not have them immediately reach for the sky on day one and produce the end product by any means necessary, which--to me as a skeptic--feels like the scope of a GAI dialog box. Of course there’s a time for low-structure creativity and open-ended design, like the final project (US parlance) or summative assessment (for those in the UK). But week to week, I generally have pretty defined expectations for the kind of patterns my students should use in their coding practice.

A side effect is that I write homework assignments that are very effective prompts for GAI. This makes my assignments ill-suited to the current environment, and my approach needs to change.

The thought does cross my mind that I could try to get genuine student responses by outlawing GAI. But honestly, I don’t expect to be able to do enforce a ban. Even if I could, I would not want to. It would create an unwelcome dynamic in the classroom, discourage students from talking about their coding process, and establish an arbitrary red line for academic misconduct that is distracting and counter-productive. No, I would rather change my methods than try to ban things.

## My perspective as a software developer

It may sound like my assessment approach is all wrong. That I should assess what students will need on the job market and in the workplace. After all, if ChatGPT can do the homeworks I assign with its eyes closed, then why should students do them? Shouldn’t they only be asked to do things that will continue to be valuable in the workplace, and that would not typically be subcontracted to GAI?

The question is fair, but it is only considering the case of a proficient, employed, experienced developer. It does not acknowledge the learning process as a process with different stages.

Think about it another way. Two things are true about real-world web development skills in 2025:

1. Most of the programming challenges I face in my day job as a web developer can’t be solved by GAI alone, or they are slower to solve with GAI, because they are too distributed, complex, and contingent on team goals, legacy systems, and discipline-specific concerns. This may change in the future, but it also may not.

2. I could not have learned to solve complex problems like I face in my day job, even with GAI, if I hadn’t first built my skills with programming by solving small, discrete challenges like the kind I was given as a student.

This is a predicament. GAI can solve many programming problems easily enough, but the solutions are only _useful_ if you know how to integrate them with a large, contextually nuanced project, and you can only learn how to do that by solving programming challenges at every level, including low-level syntax and nitty gritty bugs.

## Findings

Expecting to have these perspectives challenged, I read fifteen articles from the last year or two that broadly deal with this question. Some were empirical studies of problems and effects, some were literature reviews, and some were solutions-based proposals outlining new methods. I found some points of consensus and a few points of tension that I will try to develop a position on.

From the articles I read, the effects of tools like ChatGPT and Copilot on the coding classroom are not clear-cut, and the benefits can only be gotten with deliberate avoidance of risks. GAI can be incorporated beneficially into coding education if done intentionally, carefully, and with sophisticated forms of assessment.

Unfortunately for beginners, many of the risks coalesce around the early learning process. The literature shows that GAI can produce inaccuracies and hallucinations that novices have trouble recognizing, it can induce over-reliance on itself to the exclusion of other resources, it can solve common foundational homework-style problems, and it can offer such a variety of examples that beginners may be overwhelmed.

Some educators think these are reason enough to ban GAI in early stages of coding education, and to treat the use of GAI as an academic offense. But others say we should change the focus and structure of in-class activities and asynchronous assignments, explicitly and critically incorporating GAI as a tool where appropriate. For them, it is more realistic and responsible to teach students how to use GAI well, even when first learning to code.

In particular, for early stages of coding education, the most frequently advocated strategy is to teach students how to read and critically evaluate code, and then how to generate and adapt patterns. GAI can be used at this stage sparingly as a generation tool, to provide material for students to practice evaluating and critiquing code and its suitability for particular design goals.

Some of the literature also suggests GAI is valuable as a stand-in virtual tutor, or at least that students perceive it as such, because it can explain concepts and answer questions students have about the code they are reading or writing. While recognizing the students’ reported experiences, I am skeptical of treating GAI as a tutor, especially because some experiment-based studies found that access to GAI does not measurably improve or hamper student performance on a programming task (Xue et al.). It seems that students may perceive GAI to be a big help even when it might be a distraction.

This underscores the importance of making the risks of using GAI clear to students from the beginning. Some of the pitfalls are even self-reinforcing and harmful, like the risk of over-relying on GAI, and of using it to avoid building critical thinking skills. Perhaps the best way of addressing this dynamic is to hold open discussions early on so that students can come to individual, informed conclusions about the risks of incorporating GAI into their coding practice.

For more advanced learners, there are fewer pitfalls and more benefits. If a GAI tool provides a wealth of examples, it can be thought-provoking and informative rather than overwhelming. If it generates code with bugs, these are more easily recognized and dealt with. For programmers with a greater depth of knowledge and experience, it is less appealing to rely on GAI for everything, to the exclusion of other methods and resources. And if more advanced learners are working with larger, more complex codebases, it is more likely they will encounter problems that cannot be solved by a large language model, so they will be less susceptible to over-reliance on GAI.

One issue does seem to affect advanced learners more than beginners: the ethical issues of attribution and licensing, bias, and environmental degradation. The more generated code you publish or put into production, the more likely you are to benefit from unattributed work of others, or to surrender your authored code to use by a private training model, or to suffer from or amplify biases in the language model. And the more you ask a tool to generate, the greater your damage to the earth. So it is incumbent on us to raise these issues as critical considerations for larger projects, especially summative projects, that make use of GAI.

## Recommendations

Here is a summary of learning methods recommended by the literature that I find particularly promising:

“Explain someone else’s reasoning” (Jacques, Ouh et al., Svelka et al.). Students explain a piece of code generated by someone else without using technical language, or in their own words.

“Experiment with different approaches” (Jacques). Students generate or are presented with multiple ways of accomplishing something and are asked to compare them.

“Use multiple representations” (Jacques). For example, students get a piece of code and draw a diagram to represent the structure or meaning or effect.

Do code reviews (Svelka et al.). Students are asked to assess other students’ code and provide feedback.

Gain AI literacy (Bente, Randall, and Wäckerle). Students develop critical perspectives on the effects, opportunities, and risks of GAI, and are required explicitly to use GAI in specific assignments.

Be assessed on critical thinking (Cambaz and Zhang). Assessments are structured so that students have to demonstrate critical thinking.

Do large-scope summative projects (Bente, Randall, Wäckerle). Summative assessments require work with enough complexity or a on a large-enough scale that over-reliance on GAI is counter-productive.

## Bibliography

Albadarin, Yazid, Mohammed Saqr, Nicolas Pope, and Markku Tukiainen. “A Systematic Literature Review of Empirical Research on ChatGPT in Education.” Discover Education 3, no. 1 (May 26, 2024): 60. https://doi.org/10.1007/s44217-024-00138-2.

Becker, Brett A., Paul Denny, James Finnie-Ansley, Andrew Luxton-Reilly, James Prather, and Eddie Antonio Santos. “Programming Is Hard - Or at Least It Used to Be: Educational Opportunities and Challenges of AI Code Generation.” In Proceedings of the 54th ACM Technical Symposium on Computer Science Education V. 1, 500–506. SIGCSE 2023. New York, NY, USA: Association for Computing Machinery, 2023. https://doi.org/10.1145/3545945.3569759.

Bente, Stefan, Natasha Randall, and Dennis Wäckerle. “A Conceptual Framework to Transform Coding Education in Times of Generative AI,” 93–104. Gesellschaft für Informatik e.V., 2024. https://dl.gi.de/handle/20.500.12116/43794.

Cambaz, Doga, and Xiaoling Zhang. “Use of AI-Driven Code Generation Models in Teaching and Learning Programming: A Systematic Literature Review.” In Proceedings of the 55th ACM Technical Symposium on Computer Science Education V. 1, 172–78. SIGCSE 2024. New York, NY, USA: Association for Computing Machinery, 2024. https://doi.org/10.1145/3626252.3630958.

Crompton, Helen, and Diane Burke. “The Educational Affordances and Challenges of ChatGPT: State of the Field.” TechTrends 68, no. 2 (2024): 380–92. https://doi.org/10.1007/s11528-024-00939-0.

Israilidis, John, Wen-Yuan Chen, and Mariza Tsakalerou. “Software Development and Education: Transitioning Towards AI Enhanced Teaching.” In 2024 IEEE Global Engineering Education Conference (EDUCON), 1–6. Kos Island, Greece: IEEE, 2024. https://doi.org/10.1109/EDUCON60312.2024.10578564.

Jacques, Lorraine. “Teaching CS-101 at the Dawn of ChatGPT.” ACM Inroads 14, no. 2 (May 19, 2023): 40–46. https://doi.org/10.1145/3595634.

Jonsson, Martin, and Jakob Tholander. “Cracking the Code: Co-Coding with AI in Creative Programming Education.” In Proceedings of the 14th Conference on Creativity and Cognition, 5–14. C&amp;C ’22. New York, NY, USA: Association for Computing Machinery, 2022. https://doi.org/10.1145/3527927.3532801.

Ouh, Eng Lieh, Benjamin Kok Siew Gan, Kyong Jin Shim, and Swavek Wlodkowski. “ChatGPT, Can You Generate Solutions for My Coding Exercises? An Evaluation on Its Effectiveness in an Undergraduate Java Programming Course.” In Proceedings of the 2023 Conference on Innovation and Technology in Computer Science Education V. 1, 54–60. ITiCSE 2023. New York, NY, USA: Association for Computing Machinery, 2023. https://doi.org/10.1145/3587102.3588794.

Pang, Ashley, and Frank Vahid. “ChatGPT and Cheat Detection in CS1 Using a Program Autograding System.” In Proceedings of the 2024 on Innovation and Technology in Computer Science Education V. 1, 367–73. ITiCSE 2024. New York, NY, USA: Association for Computing Machinery, 2024. https://doi.org/10.1145/3649217.3653558.

Rahman, Md Mostafizer, and Yutaka Watanobe. “ChatGPT for Education and Research: Opportunities, Threats, and Strategies.” Applied Sciences 13, no. 9 (January 2023): 5783. https://doi.org/10.3390/app13095783.

Richards, Mike, Kevin Waugh, Mark Slaymaker, Marian Petre, John Woodthorpe, and Daniel Gooch. “Bob or Bot: Exploring ChatGPT’s Answers to University Computer Science Assessment.” ACM Trans. Comput. Educ. 24, no. 1 (January 14, 2024): 5:1-5:32. https://doi.org/10.1145/3633287.

Savelka, Jaromir, Arav Agarwal, Marshall An, Chris Bogart, and Majd Sakr. “Thrilled by Your Progress! Large Language Models (GPT-4) No Longer Struggle to Pass Assessments in Higher Education Programming Courses.” In Proceedings of the 2023 ACM Conference on International Computing Education Research - Volume 1, 1:78–92. ICER ’23. New York, NY, USA: Association for Computing Machinery, 2023. https://doi.org/10.1145/3568813.3600142.

Xie, Benjamin, Dastyni Loksa, Greg L. Nelson, Matthew J. Davidson, Dongsheng Dong, Harrison Kwik, Alex Hui Tan, Leanne Hwa, Min Li, and Amy J. Ko. “A Theory of Instruction for Introductory Programming Skills.” Computer Science Education 29, no. 2–3 (July 3, 2019): 205–53. https://doi.org/10.1080/08993408.2019.1565235.

Xue, Yuankai, Hanlin Chen, Gina R. Bai, Robert Tairas, and Yu Huang. “Does ChatGPT Help With Introductory Programming? An Experiment of Students Using ChatGPT in CS1.” In Proceedings of the 46th International Conference on Software Engineering: Software Engineering Education and Training, 331–41. ICSE-SEET ’24. New York, NY, USA: Association for Computing Machinery, 2024. https://doi.org/10.1145/3639474.3640076.
