using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Net.Http.Headers;

namespace manager.Controllers
{
    public class HomeController : Controller
    {
        private string Host = Environment.GetEnvironmentVariable("AirhornDB_URL");

        public async Task<IActionResult> Index()
        {
            var httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("MyClient", "1.0"));
            string url = String.Format("{0}/{1}", Host, "manager-config");
            //var result = await httpClient.GetStringAsync(url);
            //ViewData["Message"] = "manager-config:update-url " + result;
            var result = await GetResource("manager-config", "");

            return View(result);
        }

        public IActionResult About()
        {
            ViewData["Message"] = "Your application description page.";

            return View();
        }

        public IActionResult Contact()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult Error()
        {
            return View();
        }

        private async Task<string> GetResource(string Collection, string Key)
        {
            var httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("MyClient", "1.0"));
            var result = await httpClient.GetStringAsync(String.Format("{0}/{1}", Host, Collection));
            return result;
        }
    }
}
