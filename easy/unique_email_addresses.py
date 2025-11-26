# My solution

class Solution:
    def unique_email(self, emails: list) -> list:
        result = set()
        
        for email in emails:
            normalized = ''
            domain = False
            filter = False
            
            for char in email:
                if char == '@':
                    domain = True
                
                if domain:
                    normalized += char
                    continue
                
                if char == '+':
                    filter = True
                
                if not filter and char != '.':
                    normalized += char
                    continue
                    
            result.add(normalized)
        
        return len(result)

solution = Solution()

emails = [
    "alexsmith@example.com",
    "alex.smith@example.com",
    "alexsmith+promo@example.com",

    "mariajones@example.org",
    "maria.jones@example.org",
    "maria.jones+work@example.org",

    "david@example.net",
    "david+newsletter@example.net",

    "sarahlee@example.com",
    "sarah.lee+dev@example.com",
]

print(solution.unique_email(emails))

# Neetcode's solution

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> str:
        unique = set()
        
        for e in emails:
            # local, domain = e.split("@")
            # local = local.split("+")[0]
            # local = local.replace(".", "")
            # unique.add((local, domain))
            
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1
                
            while e[i] != "@":
                i += 1
            domain = e[i + 1:]
            unique.add((local, domain))
            
        return len(unique)