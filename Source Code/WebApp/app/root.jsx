import {
    Links,
    LiveReload,
    Meta,
    Outlet,
    Scripts,
  } from "@remix-run/react";
  
export default function App() {
    return (
    <html>
        <head>
            <link
            rel="icon"
            href="data:image/x-icon;base64,AA"
            />
            <Meta />
            <Links />
        </head> 
        <body>
            <h1>Hello okay cool!</h1>
            <Outlet />
            <Scripts />
            <LiveReload />
          </body>
        </html>
    );
}