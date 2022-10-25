
# Backend

 The [backend](https://www.geeksforgeeks.org/frontend-vs-backend/) is the server-side of the website. It stores and arranges data, and also makes sure everything on the client-side of the website works fine. It is the part of the website that you cannot see and interact with. It is the portion of software that does not come in direct contact with the users. The parts and characteristics developed by backend designers are indirectly accessed by users through a front-end application. Activities, like writing APIs, creating libraries, and working with system components without user interfaces or even systems of scientific programming, are also included in the backend.
# How the internet works
You open your favorite app on your device and you're instantly connected to the world. This is all made possible because two devices connect and communicate via a wired or wireless connection, forming something called a network. You can connect multiple devices to this network. But this becomes very complicated very quickly, as each device needs to connect to every other device to communicate effectively. This problem is solved by something called a network switch that connects multiple devices and allows them to communicate with each other. The network switch can connect to other network switches, and now two networks can connect. These network switches then connect to more network switches until you have something called an interconnected network. This interconnected network has another name that you might be familiar with. It's called the Internet

# Server
When we use websites or video streaming services on the Internet, these are provided by computers called servers.Our devices are called clients. This is known as the client-server model.  Internet connects the entire world. Have you ever had a video call with someone on another continent? That video data travel through large undersea cables connecting the world's networks. These cables can transfer huge volumes of data per second. There are a lot more technical details that go into making the Internet possible. But this is the main idea

# What is a web server and how does it work
A server is a computer that runs applications and services ranging from websites to instant messaging. It's called a server because it provides a service to another computer and its user also known as the client. Is typically stored in something called a data center with hundreds or thousands of other servers, all running different services connected to the internet. There are many different systems in data centers to ensure that servers have continuous power, continuous internet connection and are kept called 24 hours per day. Did you know that there are data centers located all around the world. Many websites use these to allow you to access your content quickly from the data center nearest to you. The data center servers are built based on the service purpose. For example, if the server is only to be used for storing images, it might have a lot of hard drive space. Whereas a server computing complex calculations might need a fast processor and a lot of memory. This is usually referred to as a server hardware. The physical components of a server. Once the server hardware is installed in the data center, a piece of code can now run. The code that runs on the hardware is commonly known as software. One way I like to remember this is to think of hardware as something you can physically touch and is difficult to change as you need to physically replace components. Software is soft or easy to change. You just replace the code running on the server. `A web server has many functions which includes website storage and administration, data storage, security and managing email. Another primary function is to handle something known as a web request. When you open a browser on your device and type the name of the website, it's the job of the web server to send you back to that website's content. This process is known as the request response cycle. Web servers are also designed to respond to thousands of requests from clients per second.`

# What are websites and webpages
A web page is a document that displays images, texts, videos and other content in the web browser, a website is a collection of webpages that link together.you can open and edit with any text editor, but developers usually use more sophisticated tools for working with webpages. If you want to work with a webpage, you need to know about three technologies and understand how they interact, their HTML, CSS and JavaScript. HTML structures the content you see, CSS controls the colors and style and JavaScript is responsible for the user interaction.HTML stands for hypertext markup language, it works by using something called markup tags. These tags describe the content that is displayed in the browser window, this content can be things like headings, paragraphs, images and even multimedia elements such as audio and video, the way html describes the content is known as markup. CSS is short for cascading style sheets and adds visual enhancements like colors and layout to the web page, this is commonly known as styling.JavaScript provides web developers with tools for interactivity, data processing, control and action. Have you ever tried to log to a website only to be told that the information you provided was incorrect or browse your favorite video streaming site and seen content update in real time? Well, that's JavaScript in action, JavaScript is the powerhouse of a web page. It has the ability to manipulate the content that you see on the screen as you interact with it. In fact, without JavaScript websites would be kind of boring and very limited in terms of what you can do, okay, you now know about the essential technologies of web page contains.`But how exactly does this code get translated to display the content that you see on your screen? When a copy of that webpage is sent from the web server to your browser, each line of code is processed in sequential order from first to last. As each line is interpreted, the browser creates the building blocks, which is the visual representation you see on the screen. This creation process is known as page rendering, the response from the web server must be a complete web page in order to fulfill the request, to show the page in the browser. `
# What is a web browser and how does it work
![Logo](/SS/SS1.png)


A web browser, or browser for short, is a software application that you use to browse the World Wide Web. It works by sending a request to a web server and then receives a response containing the content that is to be displayed on the screen of your device. Once the browser is open on your device, there is the address bar where you input the address of the website that you want to visit. The address is commonly known as the `Uniform Resource Locator` or URL for short. The URL contains the protocol or the HTTP, the domain name, usually the name of the website, and the file path, or the path to the page that is displayed. When you make a request using this URL, the browser and server communicate using a protocol known as the Hypertext Transfer Protocol or HTTP.Once the web browser receives the content, it displays it on the screen of your device. This exchange of information is made possible by something known as the request response cycle.


let me demonstrate this using an example many of us are familiar with, searching the web. First, you open a web browser, which is a software application. Next, you type the name of your favorite search engine. The name you type contains something called a domain name. Then when you press Enter, the web browser sends a request across a network and connects to another computer on the Internet called a web server. The web server is a special type of computer that allows other computers to make requests for data. The web server responds by sending a webpage back to the browser. Once the browser receives all the response information, the search engine webpage is made visible. The web page is a coded document that is rendered by the browser and then presented visually to you, the end-user. Now that the search engine webpage is loaded in the browser



# Web hosting
Web hosting is a service where you place your website and files on the hosting companies web server. You're essentially renting the space in return for stable and secure storage. You don't need to be accompanied to use a web host. Individuals can rent space too.
- shared hosting
- virtual private hosting
- dedicated hosting
- Cloud hosting

`shared hosting ==>` The cheapest form of web hosting is known as shared hosting. You pay for a location on a web server containing many web hosting accounts with shared hosting. This means that you also share the service processing power, memory, and bandwidth with other websites that might slow your performance.
![Logo](/SS/Shared_hosting.png)


`virtual private hosting ==>`A VPS is a virtual server with dedicated CPU, memory, and bandwidth resources. It will be running on a hardware server with other VPS instances but as the resources are fixed per VPS instance, your website is unlikely to be impacted by the performance of other VPS instances. A VPS instance will be more expensive than shared hosting
![Logo](/SS/vps.png)

`dedicated hosting ==>` This will be a hardware server that is dedicated to you only. All hardware, CPU, memory, and bandwidth resources are yours to use. Generally, this option is more expensive than a VPS hosting.
![Logo](/SS/dedicated.png)

`Cloud hosting ==>`Cloud hosting and the Cloud has grown in popularity over the last decade and is often mentioned in various news and services you use. With Cloud hosting, your website is run in something called a Cloud environment, which spans across multiple physical and virtual servers. If a physical or virtual server fails, your website will run on a different server and stay online. The main advantage of Cloud hosting is that you can use as many resources as you need without hardware limitations. However, you pay based on resource use. For example, if you transfer a file from the Cloud to a web browser, you'll pay for the bandwidth used for that transfer at a fractional cent cost per megabyte
![Logo](/SS/cloud_hosting.png)







