using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;


namespace manager_mvc.Models
{
    public class Scheme
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public Boolean isCurrentScheme { get; set; }
        public List<Scheme_Sound> Sounds { get; set; }
    }
}
