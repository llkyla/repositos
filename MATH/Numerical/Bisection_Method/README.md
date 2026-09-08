{\rtf1\ansi\ansicpg1252\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Bisection Method\
\
### Bisection method is one of the Root-Finding methods. \
\
##### Suppose we have an interval $[a,b]$ where $f(a) \\cdot f(b) < 0$. Then by Intermediate Value Theorem (IVT), $f(x)$ has a root in $[a, b]$. \
##### Next, we consider the mid point, $x_\{n\}=\\frac\{a_\{n\}+b_\{n\}\}\{2\}$. Get sign of $f(x_\{n\})$, and iterate the method given by $[a_\{n\}, x_\{n\}]$, or $[x_\{n\}, b_\{n\}]$. If $f(a_\{n\}) \\cdot f(x_\{n\}) > 0$, we use $[x_\{n\}, b_\{n\}]$, else we use $[a_\{n\}, x_\{n\}]$.\
##### Iterate the process until $|b_\{n\} - a_\{n\} < \\epsilon$ where $\\epsilon > 0$, represents tolerance.\
##### Order of convergence for Bisection Method is linear. }