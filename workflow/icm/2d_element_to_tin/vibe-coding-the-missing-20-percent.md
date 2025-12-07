# Vibe Coding: The Missing 20% for GIS Workflows

*How AI-assisted development transformed months of research into a polished tool in under a day*

---

## Introduction

Six months of research. Countless hours studying workflows, documentation, and edge cases. And then, in less than a day—without writing a single line of code—I had a fully functional, shareable tool with a clean user interface.

This is my experience with vibe coding, and it fundamentally changed how I think about building GIS workflows.

If you're unfamiliar with the term, **vibe coding** refers to using AI assistants to generate and orchestrate code through natural conversation. Instead of writing syntax, you describe what you want to accomplish, and the AI handles the implementation details. It's not about replacing programming knowledge—it's about leveraging that knowledge more efficiently.

For years, I've worked with visual programming tools like QGIS Model Builder and ArcGIS ModelBuilder. These are powerful tools that let you drag and drop processing steps, connecting them into automated workflows. They work well for most tasks. But there's always been a gap—a frustrating 10-20% of functionality that these tools simply can't handle elegantly.

Vibe coding fills that gap.

---

## The 80/20 Problem with Visual Programming

Anyone who has spent time in GIS knows the appeal of visual programming. Model Builder tools have been around for decades, and for good reason. You can chain together geoprocessing operations, set parameters, and create repeatable workflows—all without touching code.

For about **80-90% of typical GIS tasks**, these tools work beautifully.

But then you hit the wall.

Maybe you need conditional logic that the visual interface doesn't support well. Perhaps you want to dynamically generate output paths based on input filenames. Or you need to handle edge cases gracefully, with proper error messages and fallbacks.

The remaining **10-20%** isn't just inconvenient—it creates real problems:

- **Packaging becomes difficult.** You can build a workflow that works perfectly on your machine, but sharing it with colleagues requires extensive documentation and often manual adjustments on their end.

- **Flexibility is limited.** Visual tools are great when your workflow fits the expected pattern. The moment you need something slightly different, you're fighting against the tool instead of working with it.

- **The learning curve shifts.** Explaining a complex visual workflow to someone else can be harder than explaining equivalent code, because the visual representation often obscures the underlying logic.

I experienced all of these frustrations firsthand. I had a workflow that I could execute myself without too much trouble—I knew all the steps, all the quirks. But asking someone else to replicate it? That was another story entirely.

---

## How Vibe Coding Bridges the Gap

Here's what makes vibe coding particularly well-suited for GIS work: **it doesn't reinvent the wheel**.

When I used vibe coding to build my tool, the AI didn't write custom algorithms for spatial processing. Instead, it orchestrated calls to existing, proven tools—the same geoprocessing functions that Model Builder uses under the hood.

This is crucial for reliability. The heavy lifting—the actual spatial analysis, the geometry operations—still happens in battle-tested libraries. Vibe coding handles everything else:

- **Parameter management**: Figuring out the right arguments to pass to each tool
- **Workflow orchestration**: Connecting outputs from one step to inputs of the next
- **File handling**: Managing where intermediate and final outputs get saved
- **User interface**: Building a clean, intuitive front-end for the workflow

The result? If the output looks right, it almost certainly is right—because the core processing hasn't changed. You're not debugging novel algorithms; you're debugging configuration and flow.

And the UI aspect shouldn't be underestimated. Within my first session of vibe coding, I had a tool that not only worked correctly but also looked professional. The kind of interface that would take hours to build manually came together almost as an afterthought.

---

## My Real-World Experience

Let me be specific about what happened.

I had been working on a particular GIS workflow—on and off—for over a year. I understood all the details intimately. I had documents, notes, old QGIS project files, model files showing the steps. Everything was there, but I couldn't easily share it with anyone.

When I finally sat down with vibe coding, the transformation was remarkable:

- **Total implementation time**: Under one day (mostly within 1-3 hours of focused work)
- **Lines of code written manually**: Zero
- **Prior vibe coding experience**: This was essentially my second real project programming QGIS with Python using Cursor. I've used Cursor for a few months with mixed results on various projects.

I started by sharing my existing notes, and QGIS model files. The AI understood what I was trying to accomplish and began generating the orchestration code. When something wasn't quite right, I described the issue conversationally, and it adjusted.

The thing that struck me most was how natural it felt. I wasn't learning a new programming language or debugging cryptic error messages. I simply ran the script, pasted the error message or screenshot, and Cursor was able to troubleshoot and fix the issues. I was able to add a few more features once my prototype worked.

By the end, I had a packaged tool that I could actually share with others—something that would have taken significantly longer to build and document using traditional approaches.

---

## Beyond Code: Research and Documentation

Here's something that surprised me: vibe coding isn't just useful for building tools. It's equally powerful for research and documentation.

For example, I needed to create technical documentation comparing how my tool's triangulation approach compares to TUFLOW's method for generating smooth raster surfaces. This is specialized material—explaining Arakawa C-grid structures, vertex interpolation methods, and why TIN-based interpolation generalizes TUFLOW's fixed 4-neighbor averaging for irregular mesh topologies. It requires domain expertise to explain well.

I had the knowledge. I'd read the papers, understood the concepts, worked with the models. But translating that into clear, well-organized documentation? That's a different skill, and it takes time.

With AI assistance, I was able to produce documentation where **about 90% of the content was AI-generated**, based on my simple prompts and guidance. I verified the technical accuracy, checked the citations, and made adjustments where needed. But the heavy lifting of organizing thoughts, structuring explanations, and producing readable prose? The AI handled that.

Honestly, the result was better than what I would have written myself. Not only because the AI knows more about the topic than I do—it does since it finds excellent online resources on its own—but because it's skilled at clear explanation and logical structure. My primary contribution was fact-checking.

---

## Conclusion

If you work with GIS workflows—or really any domain where visual programming tools get you most of the way but not all the way—vibe coding deserves your attention.

It's not about replacing your expertise. It's about amplifying it.

You still need to understand your domain. You still need to know what a good workflow looks like. You still need to verify that outputs make sense. But the tedious parts—writing boilerplate code, building interfaces, wrestling with syntax—those can be handled by simply asking AI.

For me, vibe coding transformed months of accumulated knowledge into a polished, shareable tool in a matter of hours. It filled the missing 20% that visual programming couldn't reach.

If you've ever built a workflow that works perfectly for you but is nearly impossible to share with others, this approach might be exactly what you need. The barrier to trying it is low, and the potential payoff is substantial.

Give it a shot. You might be surprised by what you can build without writing a single line of code.

---

*Author's Note: In the spirit of vibe coding, this entire article was drafted by AI based on a 5-minute transcript of my verbal reflections. I provided the raw "thought data" and verified the technical accuracy; the AI handled the structure and prose. This is vibe coding in action.*

