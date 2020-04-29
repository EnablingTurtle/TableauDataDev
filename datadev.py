import tkinter as tk
import tableauserverclient as TSC

def main():
    m = tk.Tk()
    m.title('Tableau Datadev Challenge')
    scr_height = m.winfo_screenheight()/3
    scr_width = m.winfo_screenwidth()/3
    m.configure(width = scr_width, height = scr_height)

    m.grid_propagate(False)
    tk.Label(m, text='Server Address', width = 15).grid(row=1) 
    tk.Label(m, text='Token Name', width = 15).grid(row=2)
    tk.Label(m, text='Token', width = 15).grid(row=3)
    servadd = tk.Entry(m, width = 75)
    tokname = tk.Entry(m, width = 75)
    token = tk.Entry(m, width =75)
    print(servadd)
    print(tokname)
    print(token)
    output = tk.Text(m, width=65, height=15)
    buttonVal = tk.Button(m, text='Connect to Tableau', command = lambda arg1 = servadd.get(), arg2 = tokname.get(), arg3 = token.get() : connectToTab(arg1, arg2,arg3))
    servadd.grid(row=1, column=1)
    tokname.grid(row=2, column=1)
    token.grid(row=3, column=1)
    buttonVal.grid(row=4, column = 1)
    output.grid(row=6, column=0, columnspan=2)
    m.mainloop()

def connectToTab(servadd, tokname, token):
    if (servadd is None) or (tokname is None) or (token is None):
        print('missing values')
        return
    else:
        server = TSC.Server(servadd, use_server_version=True)
        tableau_auth = TSC.PersonalAccessTokenAuth(token_name=tokname,
                                                personal_access_token=token, site_id='dataforgedev786186')
        with server.auth.sign_in_with_personal_access_token(tableau_auth):
            print('Logged in successfully')
            return

main()