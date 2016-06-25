using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace manager.Models
{
    public class SoundScheme
    {
        public Guid SchemeId { get; set; }
        public string Name { get; set; }
        public Array Sounds { get; set; }
    }
}
