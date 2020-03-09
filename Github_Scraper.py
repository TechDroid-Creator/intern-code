from github import Github #pyGithub API for Github API calls
  
ACCESS_TOKEN = 'insert token here' #required for API calls

g = Github(ACCESS_TOKEN)

try:
    org=input("Enter the organisation name (org): ") #ex - google,microsoft,github
    repositories = g.search_repositories(query='org:{}'.format(org))
    req_num=int(input("\nEnter the number of top forked repos to be searched (n):"))
    m_contributors=int(input("\nEnter the number of top contributors to be searched for (m):"))


    forks_list=[]

    for repo in repositories:
        forks_list.append(repo.forks)
    forks_list.sort(reverse=True)
    #print(forks_list)

    if(len(forks_list)<req_num):
        op_forks_val=forks_list
    else:
        op_forks_val=forks_list[0:req_num]
    print("\nThe Top {} forked repositories of {} have the following number of forks respectively {}".format(req_num,org,op_forks_val))
    print("------------------------------------------------------------------------------------")

    repo_list=[]
    for val in op_forks_val :
        for repo in repositories:
            if(repo.forks==val):
                dict={}
                print("\nRepository -",repo.name)
                print("Total number of Forks -",repo.forks,"\n")
                repo_list.append(repo)
                for com in repo.get_commits():
                    if(com.committer!=None):
                        if(com.committer.login in dict.keys()):
                            dict[com.committer.login]=dict[com.committer.login]+1
                        else:
                            dict[com.committer.login]=1
                if('web-flow' in dict.keys()):
                    dict.pop('web-flow') #excluding commits made by github's web-flow
                commit_vals=list(dict.values())
                commit_vals.sort(reverse=True)
                top_n_keys=[]
                m_alternate=min(m_contributors,len(commit_vals))
                for commit_val in commit_vals[0:m_alternate]:
                    for key1 in dict.keys():
                        if(dict[key1]==commit_val):
                            top_n_keys.append(key1)
                for i in range(0,min(len(top_n_keys),len(commit_vals))):
                    print('Committer : {}\nNumber of Commits : {}\n'.format(top_n_keys[i],commit_vals[i]))
                print("------------------------------------------------------------------------------------")
except Exception as e:
    print('The following {} exception occured'.format(e))
    print("Please check the values or change token and re-run the program")
