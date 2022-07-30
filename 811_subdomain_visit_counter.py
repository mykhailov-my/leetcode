"""
Status -> Solved by myself

Time complexity -> O(N)
Space complexity -> O(N)

Solution
1. initiate dict domain -> count
2. iterate by cpdomains
    3. get vists and a domain
    4. split visits to list by '.'
    5. while list
        6. convert domain to string
        7. add string domain to dict or update counter
        8. populate top level domain from doman list
9 return converted to list of str counter dict
"""

class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counter = {}
        def add_to_counter(domains: list, count: int):
            s_domain = '.'.join(domains[::-1])
            counter[s_domain] = counter.get(s_domain, 0) + count
            domains.pop()
            return domains
        for cpdomain in cpdomains:
            visits, full_domain = cpdomain.split(' ')
            visits = int(visits)
            splitted_domain = full_domain.split('.')[::-1]
            while splitted_domain:
                add_to_counter(splitted_domain, visits)
        
        return [f'{count} {domain}' for domain, count in counter.items()]



if __name__ == '__main__':
    n = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    sol = Solution()
    res = sol.subdomainVisits(n)
    print(f'Result --> {res}')  